import sys
import math
sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")
from ECE3091_Engineering_Design.Navigation_Stack.Pin_Declaration import *


class coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y=y

#TODO make this centrepoint of ball bearing
ballCentre = coordinate(-1,-1)

# is this the real resolution?
imageWidth =  1440
imageHeight = 1080

offsetx = 0
offsety = 0

imageCentre = coordinate(math.floor(imageWidth/2)+offsetx,math.floor(imageHeight/2)+offsety)

imageError = 0.1

while ballCentre.x > imageCentre.x +imageError or ballCentre.x + imageError < imageCentre.x :
    if ballCentre.x > imageCentre.x +imageError:
        turn(-10)

    else:
        turn(10)


    time.sleep(0.1)
    ballCentre.x = -1 #new position based on NN
    ballCentre.y = -1 #new position based on NN


