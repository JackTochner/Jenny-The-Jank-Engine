from Pin_Declaration import *
from datetime import datetime

class SensorInfo:

    def __init__(self):
        self.sensorFront1 = sensorFront1.distance*100
        self.sensorFront2 = sensorFront2.distance*100
        self.sensorLeft = sensorLeft.distance*100
        self.sensorRight = sensorRight.distance*100

        self.prevSensorFront1 = None
        self.prevSensorFront2 = None
        self.prevSensorLeft = None
        self.prevSensorRight = None

        self.lastUpdate = datetime.datetime.now()


    def updateInfo(self):
        self.prevSensorFront1 = self.sensorFront1
        self.prevSensorFront2 = self.sensorFront2
        self.prevSensorLeft = self.sensorLeft
        self.prevSensorRight = self.sensorRight


        self.sensorFront1 = sensorFront1.distance*100
        self.sensorFront2 = sensorFront2.distance*100
        self.sensorLeft = sensorLeft.distance*100
        self.sensorRight = sensorRight.distance*100

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

        self.prevSensorInfo = None

def updatePos(robot,sensors):
    
    robot.pos.updateInfo()

    


    
    

    

