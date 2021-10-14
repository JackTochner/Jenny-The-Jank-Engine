import gpiozero
import time
import math
import numpy as np
import sys
rotary1 = gpiozero.RotaryEncoder(24,23, max_steps=100000)
rotary2 = gpiozero.RotaryEncoder(5,6, max_steps=100000)
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")

from ECE3091_Engineering_Design.Navigation_Stack.Pin_Declaration import *
forward = not direction1.value

direction1.value = forward
direction2.value = forward

stepsForFullTurn = 3650


pwm1Csv = csvFileCreater("pwm1Csv")
pwm1Array = []

pwm2Csv = csvFileCreater("pwm2Csv")
pwm2Array = []

xCsv = csvFileCreater("xCsv")
xArray = []

yCsv = csvFileCreater("yCsv")
yArray = []

timeCsv = csvFileCreater("timeCsv")
timeArray = []

navigationCsv = csvFileCreater("Navigation")


def obstacleCheck(gpio_echo):
    
    # USdistance = distance(gpio_echo)
    

    # print("distance: ",USdistance)

    # if (USdistance< tooClose ):
    #     print("\nobject detected? double checking...\n")
    #     pwm1.value = 0
    #     pwm2.value = 0    

    #     time.sleep(0.01)

    #     USdistance = distance(gpio_echo)

    #     print("distance: ",USdistance)

    #     # double check distances
    #     if (USdistance< tooClose):
    #         print("\nhmm, still not sure if theres an object there\n")

    #         time.sleep(0.01)

    #         USdistance = distance(gpio_echo)

    #         print("distance: ",USdistance)

    #         if (USdistance< tooClose):
    #             print("\nyep, theres an object there\n")
    #             return True

    USdistance = distance(gpio_echo)
    if(USdistance< tooClose ):
        print("object detected. Not rechecking")
        return True

    print("nope, no object detected")
    return False


def motor_simulator():
    pre_steps1=rotary1.steps
    pre_steps2=rotary2.steps
    time.sleep(0.02)

    angular1 = (2*math.pi*(rotary1.steps-pre_steps1))/(stepsForFullTurn*0.02)*1.4
    angular2 = (2*math.pi*(rotary2.steps-pre_steps2))/(stepsForFullTurn*0.02)*1.1
    return angular1,angular2
  
  
class DiffDriveRobot:
    
    def __init__(self,inertia=5, dt=0.0214, drag=0.2, wheel_radius=0.026, wheel_sep=0.102):
        
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
        print('wr')
        print(wr)
        print('wl')
        print(wl)
        w = (wr*self.r-wl*self.r)/self.l
        
        print('W\n')
        output(w)
        
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
    
    def __init__(self,Kp=3,Ki=0.1,wheel_radius=0.026, wheel_sep=0.102):
        
        self.Kp = Kp
        self.Ki = Ki
        self.r = wheel_radius
        self.l = wheel_sep
        self.e_sum_l = 0
        self.e_sum_r = 0
        
    def p_control(self,w_desired,w_measured,e_sum):
        
        #output('W_desired' + str(w_desired))
        #output('W_measured'+ str(w_measured))
        duty_cycle = min(max(-1,self.Kp*(w_desired-w_measured) + self.Ki*e_sum),1)
        #output(duty_cycle)
            
        direction = forward
        if duty_cycle < 0:
            direction = not forward
            duty_cycle = abs(duty_cycle)
        
        e_sum = e_sum + (w_desired-w_measured)
        
        return duty_cycle, e_sum, direction
        
        
    def drive(self,v_desired,w_desired,wl,wr):
        
        #output('outputs: \n')
        #output(v_desired)
        #output(w_desired)
        #output(v_desired/self.r)
        #output(self.r*w_desired/2)
        wl_desired = (v_desired-self.l/2*w_desired)/self.r
        wr_desired = (v_desired+self.l/2*w_desired)/self.r
        #output('Desired Angulars: \n')
        #output(wl_desired)
        #output(wr_desired)
        #output('n')
        
        duty_cycle_l,self.e_sum_l,direction_l = self.p_control(wl_desired,wl,self.e_sum_l)
        duty_cycle_r,self.e_sum_r,direction_r = self.p_control(wr_desired,wr,self.e_sum_r)
        
        return duty_cycle_r, duty_cycle_l, direction_r, direction_l
      
# tentacle



class TentaclePlanner:
    
    def __init__(self,dt=0.0214,steps=15,alpha=5,beta=0.1):
        
        self.dt = dt
        self.steps = steps
        # Tentacles are possible trajectories to follow
                            # rotate Left   move left       rotate right        move right           move forward    move backwards
        self.tentacles = [  (0.0,-2),      (0.1,-2),       (0.0,2),            (0.1,2),         (0.1,0.0),      (-0.1,0.0)]
        
        self.alpha = alpha
        self.beta = beta
    
    # Play a trajectory and evaluate where you'd end up
    def roll_out(self,v,w,goal_x,goal_y,goal_th,x,y,th):

        # if (w<0):            
        #     if (obstacleCheck(GPIO_ECHO_RIGHT)):
        #         return np.nan     
               
                    
        # elif(w>0):            
        #     if (obstacleCheck(GPIO_ECHO_LEFT)):
        #         return np.nan   
             

        # else:            
        #     if (obstacleCheck(GPIO_ECHO_FRONT)):
        #         return np.nan    


        #if (obstacleCheck(GPIO_ECHO_FRONT)):
        #    if (v!=0 or w> 0 ):
        #        return np.nan

        #elif (obstacleCheck(GPIO_ECHO_LEFT)):
        #    if (v!=0 or w> 0 ):
        #        return np.nan

        #elif (obstacleCheck(GPIO_ECHO_RIGHT)):
        #    if (v!=0 or w< 0 ):
        #        return np.nan

        
        
        for j in range(self.steps):
        
            x = x + self.dt*v*np.cos(th)
            y = y + self.dt*v*np.sin(th)
            th = (th + w*self.dt)

        
        

        # output("predicted x")
        # output(x)
        # output("predicted y")
        # output(y)
        
        e_th = goal_th-th
        e_th = np.arctan2(np.sin(e_th),np.cos(e_th))
        
        return self.alpha*((goal_x-x)**2 + (goal_y-y)**2) + self.beta*(e_th**2)
    
    # Choose trajectory that will get you closest to the goal
    def plan(self,goal_x,goal_y,goal_th,x,y,th):
        
        costs =[]
        for v,w in self.tentacles:
            costs.append(self.roll_out(v,w,goal_x,goal_y,goal_th,x,y,th))
        
        best_idx = np.nanargmin(costs)

        output(self.tentacles[best_idx])
        
        return self.tentacles[best_idx]
      
robot = DiffDriveRobot()
controller = RobotController()
planner = TentaclePlanner()

poses = []
velocities = []
duty_cycle_commands = []



#output(goal_x)
#output(goal_y)
#output(goal_th)



def Navigate(x,y,th):

    goal_x = x
    goal_y = y
    goal_th = th

    while True:
        i = 0

        # Plan using tentacles
        v,w = planner.plan(goal_x,goal_y,goal_th,robot.x,robot.y,robot.th)
        
        duty_cycle_l,duty_cycle_r,direction_l,direction_r = controller.drive(v,w,robot.wl,robot.wr)
        pwm1.value,pwm2.value,direction1.value,direction2.value = controller.drive(v,w,robot.wl,robot.wr)

        output(direction1.value)
        output(direction2.value)

        if direction1.value == 0:
            direction1Value = -1
        else:
            direction1Value = 1


        if direction2.value == 0:
            direction2Value = -1
        else:
            direction2Value = 1

        
        pwm1Array.append(pwm1.value*(direction1Value))
        pwm2Array.append(pwm2.value*(direction2Value))
        
        # Simulate robot motion - send duty cycle command to robot
        x,y,th = robot.pose_update()
        
        print('X position \n')
        output(x)
        
        xArray.append(x)

        print('Y position \n')
        output(y)
        
        print('Th position \n')
        output(th*(180/math.pi))

        yArray.append(y)

        # Log data
        poses.append([x,y,th])
        duty_cycle_commands.append([duty_cycle_l,duty_cycle_r])
        velocities.append([robot.wl,robot.wr])

        #output("goal_x-x")
        #output(goal_x-x)
        #output("goal_y-y")
        #output(goal_y-y) 
        #output("goal_th-th")
        #output((goal_th-th)*(180/math.pi))

        timeArray.append(i)

        if abs(goal_th-th)<0.01 and abs(goal_x-x) < 0.02 and abs(goal_y-y) < 0.02:
            break

        i += 1

    

outputcsv(pwm1Csv,pwm1Array)
outputcsv(pwm2Csv,pwm2Array)
outputcsv(xCsv,xArray)
outputcsv(yCsv,yArray)
outputcsv(timeCsv,timeArray)

outputcsv(navigationCsv,timeArray)
outputcsv(navigationCsv,pwm1Array)
outputcsv(navigationCsv,pwm2Array)
outputcsv(navigationCsv,xArray)
outputcsv(navigationCsv,yArray)


Navigate(0,0,90*(math.pi/180))


