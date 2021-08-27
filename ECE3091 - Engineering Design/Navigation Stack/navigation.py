import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from IPython import display
import time


pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)
encoder = gpiozero.RotaryEncoder(a=5, b=6,max_steps=100000) 

w = 0
w_desired = 2.0
w_measured = 0.0
duty_cycle = 0

e_sum = 0.0
rot_vel = 0.0

#diff drive robot model class
class DiffDriveRobot:

    def __init__(self,inertia=5, dt=0.1, drag=0.2, wheel_radius=0.05, wheel_sep=0.15):
        
        self.x = 0.0 # y-position
        self.y = 0.0 # y-position 
        self.th = 0.0 # orientation 
        
        self.wl = rot_vel #placeholder variable for rotational velocity 
        self.wr = rot_vel #rotational velocity right wheel
        
        self.I = inertia
        self.d = drag
        self.dt = dt
        
        self.r = wheel_radius
        self.l = wheel_sep
    
# Should be replaced by motor encoder measurement which measures how fast wheel is turning
# Here, we simulate the real system and measurement

# def motor_simulator(self,w,duty_cycle):
    
#     torque = self.I*duty_cycle
    
#     if (w > 0):
#         w = min(w + self.dt*(torque - self.d*w),3)
#     elif (w < 0):
#         w = max(w + self.dt*(torque - self.d*w),-3)
#     else:
#         w = w + self.dt*(torque)
    
#     return w

# Veclocity motion model
def base_velocity(self,wl,wr):
    
    v = (wl*self.r + wr*self.r)/2.0
    
    w = (wl - wr)/self.l
    
    return v, w

# Kinematic motion model
def pose_update(self,duty_cycle_l,duty_cycle_r):
    
    self.wl = self.motor_simulator(self.wl,duty_cycle_l)
    self.wr = self.motor_simulator(self.wr,duty_cycle_r)
    
    v, w = self.base_velocity(self.wl,self.wr)
    
    self.x = self.x + self.dt*v*np.cos(self.th)
    self.y = self.y + self.dt*v*np.sin(self.th)
    self.th = self.th + w*self.dt
    
    return self.x, self.y, self.th

class RobotController:
    
    def __init__(self,Kp=0.1,Ki=0.01,wheel_radius=0.02, wheel_sep=0.1): #should be changed to match our robot's parameters
        
        self.Kp = Kp
        self.Ki = Ki
        self.r = wheel_radius
        self.l = wheel_sep
        self.e_sum_l = 0
        self.e_sum_r = 0
        
    def p_control(self,w_desired,w_measured,e_sum):
        
        duty_cycle = min(max(-1,self.Kp*(w_desired-w_measured) + self.Ki*e_sum),1)
        
        e_sum = e_sum + (w_desired-w_measured)
        
        return duty_cycle, e_sum
        
        
    def drive(self,v_desired,w_desired,wl,wr):
        
        wl_desired = v_desired/self.r + self.l*w_desired/2 
        wr_desired = v_desired/self.r - self.l*w_desired/2
        
        duty_cycle_l,self.e_sum_l = self.p_control(wl_desired,wl,self.e_sum_l)
        duty_cycle_r,self.e_sum_r = self.p_control(wr_desired,wr,self.e_sum_r)
        
        return duty_cycle_l, duty_cycle_r

#calling classes
robot = DiffDriveRobot(inertia=5, dt=0.1, drag=1, wheel_radius=0.05, wheel_sep=0.15)
controller = RobotController(Kp=1,Ki=0.25,wheel_radius=0.05,wheel_sep=0.15)

#motion
for i in range(300):

    # Example motion using controller 
    
    if i < 100: # drive in circular path (turn left) for 10 s
        pwml,pwm2 = controller.drive(0.1,1,robot.wl,robot.wr)
    elif i < 200: # drive in circular path (turn right) for 10 s
        pwm1,pwm2 = controller.drive(0.1,-1,robot.wl,robot.wr)
    else: # stop
        pwm1,pwm2 = (0,0)
    
    # Simulate robot motion - send duty cycle command to robot
    x,y,th = robot.pose_update(pwm1,pwm2)
    