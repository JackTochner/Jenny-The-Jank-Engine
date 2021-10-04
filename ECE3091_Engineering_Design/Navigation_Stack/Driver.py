import os
from datetime import datetime
import sys

sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")
from ECE3091_Engineering_Design.Navigation_Stack.Alignment import GPIO_ECHO_FRONT1
from Pin_Declaration import *
from Mapping import *
from Alignment import Align

# need to check if importing only the function will work...

#from Navigation_Main import *
from Navigation import *
from SearchMode import *



def main(align = False, navigate = False, comp=False):



    if align:   
        output("Starting Alignment...")

        Align()

        output("Finished Alignement")

    if navigate:
        output("Starting Navigation")

        Navigate(0,0,-math.pi)

        output("Finished Navigation")

    if comp:
        output("Starting Search...")
        #search()
        output("Finished")


    while True:
        distanceFront = distance(GPIO_ECHO_FRONT1)
        distanceLeft = distance(GPIO_ECHO_LEFT)
        distanceRight = distance(GPIO_ECHO_RIGHT)

        print("distanceFront: ", distanceFront, "distanceLeft: ", distanceLeft, "distanceRight: ", distanceRight)

        time.sleep(0.2)

f.close()

