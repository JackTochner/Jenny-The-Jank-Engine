
import numpy as np
import time
from Pin_Declaration import *
import math

#initialising values
duty_cycle = 0
e_sum = 0.0
ang_vel = 0.0
maxSteps = 3650

rotary1 = gpiozero.RotaryEncoder(5,6, max_steps=100000)
rotary2 = gpiozero.RotaryEncoder(23,24, max_steps=100000)

def findAngular():    
    pre_steps1=rotary1.steps
    pre_steps2 = rotary2.steps
    time.sleep(0.1)
    angular_l = (2*math.pi*(rotary1.steps-pre_steps1))/(maxSteps*0.1)
    angular_r = (2*math.pi*(rotary2.steps-pre_steps2))/(maxSteps*0.1)

    print("angular_l: ", angular_l, "angular_r: ", angular_r, "\n")
    return angular_l, angular_r

#diff drive robot model class
class DiffDriveRobot:

    def __init__(self,inertia=5, dt=0.1, drag=0.2, wheel_radius=0.05, wheel_sep=0.15):
        
        self.x = 0.0 # y-position
        self.y = 0.0 # y-position 
        self.th = 0.0 # orientation 
        
        self.wl = ang_vel #placeholder variable for rotational velocity 
        self.wr = ang_vel 
        
        self.I = inertia
        self.d = drag
        self.dt = dt
        
        self.r = wheel_radius
        self.l = wheel_sep
    
    # Should be replaced by motor encoder measurement which measures how fast wheel is turning
    # Here, we simulate the real system and measurement
    # Veclocity motion model
    def base_velocity(self,wl,wr):
        
        v = (wl*self.r + wr*self.r)/2.0
        
        w = (wl - wr)/self.l
        
        return v, w

    # Kinematic motion model
    def pose_update(self,duty_cycle_l,duty_cycle_r):
        
        self.wl,self.wr = findAngular()

        v, w = self.base_velocity(self.wl,self.wr)
        
        self.x = self.x + self.dt*v*np.cos(self.th)
        self.y = self.y + self.dt*v*np.sin(self.th)
        self.th = self.th + w*self.dt
        
        return self.x, self.y, self.th

class RobotController:
    
    def __init__(self,Kp=0.07,Ki=0.01,wheel_radius=0.02, wheel_sep=0.10): 
        
        self.Kp = Kp
        self.Ki = Ki
        self.r = wheel_radius
        self.l = wheel_sep
        self.e_sum_l = 0
        self.e_sum_r = 0
        
    def p_control(self,w_desired,w_measured,e_sum):
        print("w_desired: " , w_desired, "w_measured: ", w_measured, "e_sum: ", e_sum, "\n")

        print(self.Kp*(w_desired-w_measured) + self.Ki*e_sum)

        duty_cycle = min(max(-1,(self.Kp*(w_desired-w_measured) + self.Ki*e_sum)),1)

        #duty_cycle = min(max(-1,(self.Kp*(w_desired-w_measured) )),1)

        direction = forward
        if duty_cycle < 0:
            direction = not forward
            duty_cycle = abs(duty_cycle)
        
        e_sum = e_sum + (w_desired-w_measured)
        
        return duty_cycle, e_sum, direction
        
        
    def drive(self,v_desired,w_desired,wl,wr):
        
        wl_desired = v_desired/self.r + self.l*w_desired/2 
        wr_desired = v_desired/self.r - self.l*w_desired/2
        
        print("left:")
        duty_cycle_l,self.e_sum_l,direction_l = self.p_control(wl_desired,wl,self.e_sum_l)

        print("right:")
        duty_cycle_r,self.e_sum_r ,direction_r= self.p_control(wr_desired,wr,self.e_sum_r)
        
        return duty_cycle_l, duty_cycle_r, direction_l, direction_r

#calling classes
robot = DiffDriveRobot(inertia=5, dt=0.1, drag=1, wheel_radius=0.028, wheel_sep=0.105)
controller = RobotController(Kp=1,Ki=0.25,wheel_radius=0.028,wheel_sep=0.105)

#motion
for i in range(100):

    print("\n")

    # # Example motion using controller 
    # if i < 37: # drive in circular path (turn left) for 10 s
    #     pwm1.value,pwm2.value,direction1.value,direction2.value= controller.drive(0.1,0,robot.wl,robot.wr) #go straight for 3 secs
       
    if i < 100: 
         pwm1_new,pwm2_new,direction1.value,direction2.value= controller.drive(0.1,50,robot.wl,robot.wr) # 90 deg turn
         if pwm1_new != pwm2_new:
             pwm1.value = pwm1_new
             pwm2.value = pwm2_new
        
    # elif i < 80:  # drive in circular path (turn right) for 10 s
    #     pwm1.value,pwm2.value,direction1.value,direction2.value = controller.drive(0.1,0,robot.wl,robot.wr) # go straight for another 30 sec
        
    else:
        pwm1.value,pwm2.value = (0,0)
    
    print("pwm1: ", pwm1.value, " pwm2: ", pwm2.value, " direction1: " , direction1.value , " direction2: " , direction2.value , "\n")
    
    #time.sleep(0.1)

    #update values
    x,y,th= robot.pose_update(pwm1.value,pwm2.value)
    
print("navigation finished")
