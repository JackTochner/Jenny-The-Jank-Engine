import multiprocessing
import gpiozero
import time
import math
import numpy as np
import sys

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


def obstacleCheck(USdistance): 
    
    

    # print("distance: ",USdistance)

    # if (USdistance< tooClose ):
    #     print("\nobject detected? double checking...\n")
  

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

    
    if(USdistance< tooClose ):
        print("object detected. Not rechecking")
        return True

    #print("nope, no object detected")
    return False


def motor_simulator(rotary1,rotary2):
    pre_steps1=rotary1.steps
    pre_steps2=rotary2.steps
    time.sleep(0.02)

    angular1 = (2*math.pi*(rotary1.steps-pre_steps1))/(stepsForFullTurn*0.02)*1.5
    angular2 = (2*math.pi*(rotary2.steps-pre_steps2))/(stepsForFullTurn*0.02)*1.6

    #print("angular1: ", angular1, " angular2: ", angular2)
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
        
        w = (wr*self.r-wl*self.r)/self.l
        
        #print('W\n')
        #output(w)
        
        return v, w
    
    # Kinematic motion model
    def pose_update(self,rotary1,rotary2):
        
        self.wr,self.wl = motor_simulator(rotary1,rotary2)
        
        v, w = self.base_velocity(self.wl,self.wr)

        #print("v: ",v)
        
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
        self.tentacles = [  (0.0,-2),      (0.1,-2),       (0.0,2),            (0.1,2),             (0.1,0.0)                       ]
        
        self.alpha = alpha
        self.beta = beta
    
    # Play a trajectory and evaluate where you'd end up
    def roll_out(self,v,w,goal_x,goal_y,goal_th,x,y,th,distanceLeft,distanceRight,distanceFront,obstacleDetected,onlyturn):


        
        if (obstacleDetected[0]): #left US
            if (v!=0 or w> 0 ):              
                return np.nan

        elif (obstacleDetected[1]): #front US
            if (v!=0):         
                return np.nan

        elif (obstacleDetected[2]): #right US
            if (v!=0 or w< 0 ):         
                return np.nan

        

        # if onlyturn:
        #     print("onlyturn is on")
        #     if v !=0 :
        #         return np.nan

        # else:
        #     if (v == 0):
        #         return np.nan
        
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
    def plan(self,goal_x,goal_y,goal_th,x,y,th,distances,obstacleDetected,onlyturn):
        
        costs =[]

        # distanceFront = distance(GPIO_ECHO_FRONT)
        # distanceLeft = distance(GPIO_ECHO_LEFT)
        # distanceRight = distance(GPIO_ECHO_RIGHT)

        distanceFront = distances[0]
        distanceLeft = distances[1]
        distanceRight = distances[2]

        #print("Front: ", distanceFront, " Left: ", distanceLeft, " Right: ", distanceRight)

        # distanceFront = 500
        # distanceLeft = 500
        # distanceRight = 500

        for v,w in self.tentacles:
            costs.append(self.roll_out(v,w,goal_x,goal_y,goal_th,x,y,th,distanceLeft,distanceRight,distanceFront,obstacleDetected,onlyturn))
        
        best_idx = np.nanargmin(costs)

        #output(self.tentacles[best_idx])
        
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



def Navigate(x,y,th,distances,obstacleDetected,foundObject):

    goal_x = x
    goal_y = 0
    goal_th = 0    

    rotary1 = gpiozero.RotaryEncoder(24,23, max_steps=100000)
    rotary2 = gpiozero.RotaryEncoder(5,6, max_steps=100000)

    pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000) #Right
    pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000) #Left




    def turn(degree):
        degPerSec = 62
        if degree < 0:
            degree = abs(degree)
            for i in range(round((degree/degPerSec)*10)):

                print("turning right")            
                pwm1.value = 1
                pwm2.value = 1     

                direction1.value = not forward       

                time.sleep(0.1)

        else:
            for i in range(round((degree/degPerSec)*10)):

                print("turning left")            
                pwm1.value = 1
                pwm2.value = 1

                direction2.value = not forward

                time.sleep(0.1)

        direction1.value = forward
        direction2.value = forward

    
    def driveToBall(x,y,w,h):

        
        x = x-600
        y = y-360

        print("turning...")
        turn(-x*45/600)

        pwm1.value = 0
        pwm2.value = 0

        print("now facing ball. sleeping for 2 seconds...")
        #time.sleep(2)


        pwm1.value = 1
        pwm2.value = 1
        print("moving forward for 20 seconds")

        time.sleep(20)
        


    onlyturn = False

    turn(goal_th)

    i = 0
    
    while True:     
        i+=1
        

        start = time.time()
        

        # Plan using tentacles
        v,w = planner.plan(goal_x,goal_y,goal_th,robot.x,robot.y,robot.th,distances,obstacleDetected,onlyturn)
        
        duty_cycle_l,duty_cycle_r,direction_l,direction_r = controller.drive(v,w,robot.wl,robot.wr)


        pwm1.value,pwm2.value,direction1.value,direction2.value = controller.drive(v,w,robot.wl,robot.wr)
        # pwm1.value = pwm1.value*0.998
        # pwm2.value = pwm2.value*0.999 


        #output(direction1.value)
        #output(direction2.value)

        if direction1.value == 0:
            direction1Value = -1
        else:
            direction1Value = 1


        if direction2.value == 0:
            direction2Value = -1
        else:
            direction2Value = 1

        
        #pwm1Array.append(pwm1.value*(direction1Value))
        #pwm2Array.append(pwm2.value*(direction2Value))
        
        # Simulate robot motion - send duty cycle command to robot
        xpos,ypos,thpos = robot.pose_update(rotary1,rotary2)
        
    
        #print('x: ',xpos, ", y: ", ypos, ", th: ", thpos*(180/math.pi))

        
        
        # xArray.append(x)

        # print('Y')
        # print(ypos)
        
        # print('th')
        # output(thpos*(180/math.pi))

        #print("pwm1: ", pwm1.value, " pwm2: ", pwm2.value)

        

        #yArray.append(y)

        # Log data
        # poses.append([x,y,th])
        # duty_cycle_commands.append([duty_cycle_l,duty_cycle_r])
        # velocities.append([robot.wl,robot.wr])

        # output("goal_x-x")
        # output(goal_x-x)
        # output("goal_y-y")
        # output(goal_y-y) 
        # output("goal_th-th")
        # output(goal_th-th)
        #timeArray.append(i)

        if thpos*(180/math.pi) >= 360 or thpos*(180/math.pi) <= -360:
            thpos = 0
            robot.th = 0

        #and abs(goal_y-ypos) < 0.05
        if abs(goal_x-xpos) < 0.01 :
            print("reached goal")

            turn(-90)

            

            # for i in range(200):

            #     if i %10 == 0:
            #         print("waiting")
            #     pwm1.value = 0
            #     pwm2.value = 0
            #     time.sleep(0.01)
           
            #goal_x = 0.3
            #goal_y = -0.3
            controller.e_sum_l = 0
            controller.e_sum_r = 0
            robot.x = 0
            robot.y=0
            robot.th = 0


        # if  abs(goal_th-thpos)< 0.1 and abs(goal_x-xpos) < 0.01 and abs(goal_y-ypos) < 0.05:

        # #if abs(goal_th-th) < 0.1 and abs(goal_x-x) < 0.01 and abs(goal_y-y) < 0.05:
        #     goal_x
            
            

        #i += 1

        stop = time.time()

        totalTime= stop-start

        # if totalTime <= 0.1:
        #     time.sleep(0.1-totalTime)
        # else:
        #     #print("TOTAL TIME GREATER THAN 0.1: ", totalTime)
        #     pass

        if foundObject[0]:
            print("OBJECT FOUND IN NN!!!!!! - from Nav")
            print("Jenny is celebrating")

            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])

            
            break
     
        
        #print("dt = ",totalTime, ' \n')

    

# outputcsv(pwm1Csv,pwm1Array)
# outputcsv(pwm2Csv,pwm2Array)
# outputcsv(xCsv,xArray)
# outputcsv(yCsv,yArray)
# outputcsv(timeCsv,timeArray)

# outputcsv(navigationCsv,timeArray)
# outputcsv(navigationCsv,pwm1Array)
# outputcsv(navigationCsv,pwm2Array)
# outputcsv(navigationCsv,xArray)
# outputcsv(navigationCsv,yArray)



def USTEST(distances):
    while True:
        #print()
        distanceFront = distances[0]
        distanceLeft = distances[1]
        distanceRight = distances[2]

        #print("Front: ", distanceFront, " Left: ", distanceLeft, " Right: ", distanceRight)

if __name__ == '__main__':


    
    with Manager() as manager:

       distances = manager.list([500,500,500])
       obstacleDetected = manager.list([False,False,False])

       US = Process(target = distance, args = (distances,obstacleDetected))

       nav = Process(target = Navigate, args = (0.5,0,0,distances,obstacleDetected))

       #test = Process(target = USTEST, args = (distances,))

       US.start()
       #test.start()
       nav.start()

       US.join()
       #test.start()
       nav.join()

       while True:
           if not US.is_alive:
               print("Ultrasonics are dead")


        # d = manager.dict()
        # l = manager.list(range(10))

        # p = Process(target=f, args=(d, l))
        # p.start()
        # p.join()

        # print(d)
        # print(l)





