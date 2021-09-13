
import gpiozero
import time
import math
import numpy as np


rotary1 = gpiozero.RotaryEncoder(23,24, max_steps=100000)
rotary2 = gpiozero.RotaryEncoder(5,6, max_steps=100000)

pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)
forward = direction1.value

direction1.value = forward
direction2.value = forward

stepsForFullTurn = 3650


def motor_simulator():
  pre_steps1=rotary1.steps
  pre_steps2=rotary2.steps
  time.sleep(0.01)
  
  angular1 = (2*math.pi*(rotary1.steps-pre_steps1))/(stepsForFullTurn*0.01)
  angular2 = (2*math.pi*(rotary2.steps-pre_steps2))/(stepsForFullTurn*0.01)
    
  return angular1,angular2
  
  
class DiffDriveRobot:
    
    def __init__(self,inertia=5, dt=0.1, drag=0.2, wheel_radius=0.026, wheel_sep=0.13):
        
        self.x = 0.0 # y-position
        self.y = 0.0 # y-position 
        self.th = 0.0 # orientation
        
        self.wl = 0.0 #rotational velocity left wheel
        self.wr = 0.0 #rotational velocity right wheel
        
        self.I = inertia
        self.d = drag
        self.dt = dt
        
        self.r = wheel_radius
        self.l = wheel_sep

        
    # Veclocity motion model
    def base_velocity(self,wl,wr):
        
        v = (wl*self.r + wr*self.r)/2.0
        
        w = (wl - wr)/self.l
        
        return v, w
    
    # Kinematic motion model
    def pose_update(self):
        
        self.wr,self.wl = motor_simulator()
        
        v, w = self.base_velocity(self.wl,self.wr)
        
        self.x = self.x + self.dt*v*np.cos(self.th)
        self.y = self.y + self.dt*v*np.sin(self.th)
        self.th = self.th + w*self.dt
        
        return self.x, self.y, self.th


class RobotController:
    
    def __init__(self,Kp=1.0,Ki=0.001,wheel_radius=0.026, wheel_sep=0.13):
        
        self.Kp = Kp
        self.Ki = Ki
        self.r = wheel_radius
        self.l = wheel_sep
        self.e_sum_l = 0
        self.e_sum_r = 0
        
    def p_control(self,w_desired,w_measured,e_sum):
        
        print('W_desired',w_desired)
        print('W_measured',w_measured)
        duty_cycle = min(max(-1,self.Kp*(w_desired-w_measured) + self.Ki*e_sum),1)
        print(duty_cycle)
            
        direction = forward
        if duty_cycle < 0:
            direction = not forward
            duty_cycle = abs(duty_cycle)
        
        e_sum = e_sum + (w_desired-w_measured)
        
        return duty_cycle, e_sum, direction
        
        
    def drive(self,v_desired,w_desired,wl,wr):
        
        print('outputs: \n')
        print(v_desired)
        print(w_desired)
        print(v_desired/self.r)
        print(self.r*w_desired/2)
        wl_desired = v_desired/self.r + self.r*w_desired/2 
        wr_desired = v_desired/self.r - self.r*w_desired/2
        print('Desired Angulars: \n')
        print(wl_desired)
        print(wr_desired)
        print('n')
        
        duty_cycle_l,self.e_sum_l,direction_l = self.p_control(wl_desired,wl,self.e_sum_l)
        duty_cycle_r,self.e_sum_r,direction_r = self.p_control(wr_desired,wr,self.e_sum_r)
        
        return duty_cycle_r, duty_cycle_l, direction_r, direction_l
    
    
robot = DiffDriveRobot()
controller = RobotController()

poses = []
velocities = []
duty_cycle_commands = []


for i in range(1000):

    # Example motion using controller 
    
    if i < 500: # drive in circular path (turn left) for 10 s
        duty_cycle_l,duty_cycle_r,direction_l,direction_r = controller.drive(0.1,100,robot.wl,robot.wr)
        pwm1.value,pwm2.value,direction1.value,direction2.value = controller.drive(0.01,10,robot.wl,robot.wr)

    elif i < 1000: # drive in circular path (turn right) for 10 s
        duty_cycle_l,duty_cycle_r,direction_l,direction_r = controller.drive(0.1,-100,robot.wl,robot.wr)
        pwm1.value,pwm2.value,direction1.value,direction2.value = controller.drive(0.01,-10,robot.wl,robot.wr)

    else: # stop
        duty_cycle_l,duty_cycle_r,direction_l,direction_r = controller.drive(0,0,robot.wl,robot.wr)
        pwm1.value,pwm2.value,direction1.value,direction2.value = controller.drive(0,0)

        
    x,y,th = robot.pose_update()
    
    # Log data
    poses.append([x,y,th])
    duty_cycle_commands.append([duty_cycle_l,duty_cycle_r])
    velocities.append([robot.wl,robot.wr])
    
