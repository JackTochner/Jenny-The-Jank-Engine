import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from IPython import display
import time

# GitHub is working!

def pwm_control(w_desired,w_measured,Kp,Ki,e_sum):
    
    duty_cycle = min(max(0,Kp*(w_desired-w_measured) + Ki*e_sum),1)
    e_sum = e_sum + w_desired-w_measured
    
    return duty_cycle, e_sum

def motor_simulator(w,duty_cycle):

    I = 5
    dt = 0.1
    d = 1
    
    torque = I*duty_cycle

    if (w > 0):
        w = min(w + dt*(torque - d*w),3)
    elif (w < 0):
        w = max(w + dt*(torque - d*w),-3)
    else:
        w = w + dt*(torque)

    return w


w = 0
w_desired = 2.0
w_measured = 0.0
duty_cycle = 0


plt.figure(figsize=(15,5))

e_sum = 0

#plt.show()
plt.ion()
#fig.canvas.draw()
plt.show(block=False)
fig = plt.figure()

for j in range(50):
    
    
    duty_cycle,e_sum = pwm_control(w_desired,w_measured,Kp=1.0,Ki=0.25,e_sum=e_sum)
    
    w_measured = motor_simulator(w_measured,duty_cycle)    
   
    ax1 = fig.add_subplot(1,2,1)

    line1 = ax1.plot(j,w_measured,'bo')
    line2 = ax1.plot(j,w_desired,'r+')
    
    
    ax2 = fig.add_subplot(1,2,2)
    line3 = ax2.plot(j,duty_cycle,'bo')
    fig.canvas.draw()

    time.sleep(0.1)

    fig.canvas.flush_events()
    
    # display.clear_output(wait=True)
    # display.display(fig.gcf())


#diff drive robot model
class DiffDriveRobot:

    def __init__(self,inertia=5, dt=0.1, drag=0.2, wheel_radius=0.05, wheel_sep=0.15):
        
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
    
# Should be replaced by motor encoder measurement which measures how fast wheel is turning
# Here, we simulate the real system and measurement
def motor_simulator(self,w,duty_cycle):
    
    torque = self.I*duty_cycle
    
    if (w > 0):
        w = min(w + self.dt*(torque - self.d*w),3)
    elif (w < 0):
        w = max(w + self.dt*(torque - self.d*w),-3)
    else:
        w = w + self.dt*(torque)
    
    return w

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