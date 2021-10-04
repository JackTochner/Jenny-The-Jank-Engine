from Pin_Declaration import *
from datetime import datetime
import time
from Alignment import align
import csv

class SensorInfo:

    def __init__(self):
        self.sensorFront1 = distance(GPIO_ECHO_FRONT1)
        self.sensorFront2 = distance(GPIO_ECHO_FRONT2)
        #self.sensorLeft = sensorLeft.distance*100
        #self.sensorRight = sensorRight.distance*100

        self.prevSensorFront1 = None
        self.prevSensorFront2 = None
        #self.prevSensorLeft = None
        #self.prevSensorRight = None

        self.lastUpdate = datetime.datetime.now()

        self.sensorFront1Array = []
        self.sensorFront2Array = []
        #self.sensorLeftArray = []
        #self.sensorRightArray = []
        


    def updateInfo(self):
        self.prevSensorFront1 = self.sensorFront1
        self.prevSensorFront2 = self.sensorFront2
        #self.prevSensorLeft = self.sensorLeft
        #self.prevSensorRight = self.sensorRight


        self.sensorFront1 = distance(GPIO_ECHO_FRONT1)
        self.sensorFront2 = distance(GPIO_ECHO_FRONT2)
        #self.sensorLeft = sensorLeft.distance*100
        #self.sensorRight = sensorRight.distance*100

        
        self.sensorFront1Array.append(self.sensorFront1)
        self.sensorFront2Array.append(self.sensorFront2)
        #self.sensorLeftArray.append(self.sensorLeft)
        #self.sensorRightArray.append(self.sensorRight)

        self.lastUpdateDif = (datetime.datetime.now() - self.lastUpdate).total_seconds()

        self.lastUpdate = datetime.datetime.now()

        
class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Map:  
    
    def __init__(self,robot,goal,obstacles = []):
        self.robot = robot
        self.goal = goal
        
        self.obstacles = []
        for i in range(len(obstacles)):
            self.obstacles.append(obstacles[i])

        self.heading = 0

class Jenny:

    def __init__(self, heading):
        self.pos = SensorInfo()
        self.heading = heading
        self.vel = 0
        self.rotVel = 0
        self.start = SensorInfo()

        self.posDif = ((self.pos.sensorFront1-self.start.sensorFront1)+(self.pos.sensorFront2-self.start.sensorFront1))/2

        self.prevSensorInfo = None

        self.sensorDifErr = 0.5

    def updatePosDif(self):

        while abs(self.pos.sensorFront1 - self.pos.sensorFront2) > self.sensorDifErr:
            time.sleep(0.1)
            self.pos.updateInfo
        self.posDif = ((self.pos.sensorFront1-self.start.sensorFront1)+(self.pos.sensorFront2-self.start.sensorFront1))/2

def prelim():
    jenny = Jenny()

    pwm1.value = 0.5
    pwm2.value = 0.5

    time.sleep(0.5)

    jenny.pos.updateInfo()
    jenny.updatePosDif()
    while jenny.posDif < 30:
        jenny.pos.updateInfo()
        jenny.updatePosDif()
        time.sleep(0.1)

    turnRight()

    align()

    jenny.start.updateInfo()
    time.sleep(0.1)
    jenny.pos.updateInfo()

    while jenny.posDif < 30:
        jenny.pos.updateInfo()
        jenny.updatePosDif()
        time.sleep(0.1)

    f_prelim_csv = open("prelim.csv","w")    

    writer = csv.writer(f_prelim_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    writer.writerow(jenny.pos.sensorFront1Array)
    writer.writerow(jenny.pos.sensorFront2Array)
    #writer.writerow(jenny.pos.sensorLeftArray)
    #writer.writerow(jenny.pos.sensorRightArray)



def turnRight():
    direction2.value = not direction2.value
    time.sleep(0.5)
    direction2.value = not direction2.value


    




    
    

    

