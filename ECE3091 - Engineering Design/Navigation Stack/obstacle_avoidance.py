from Pin_Declaration import *
import math


def obstacle_avoid():

    #ASSUMPTIONS:
    # - robot is aligned before obstacle avoidance starts
    # - any object is large enough such that, if the object is in front of the robot, and within the close value, at least one of the sensors will detect it

    while True:

        distanceRight = sensorRight.distance * 100 
        distanceLeft = sensorLeft.distance * 100
        distanceFront1 = sensorFront1.distance * 100 
        distanceFront2 = sensorFront2.distance * 100 

        # move forward
        pwm1.value = 0.5
        pwm2.value = 0.5

        # Variable used to define how close an object will need to be before the robot will turn away
        close = 10


        # Detect Objects in relation to Robot
        print("trying to detect objects...")


        # Case: about to hit a wall
        if distanceFront1 + error < 3 and distanceFront2 + error < 3 and distanceLeft + error< 3/(math.sqrt(2)/2) and distanceRight + error < 3/(math.sqrt(2)/2):
            print("wall found. stopping...")
            pwm1.value = 0
            pwm2.value = 0
            break

        # Case: object only covering one front sensor

        #object is in front on the right half of the robot
        elif distanceFront1 > distanceFront2 + error and distanceFront2+error < close: 
            print("object detected on right side")

            while distanceFront1 > distanceFront2 + error and distanceFront2+error < close:
                direction1 = not direction1

                distanceFront1 = sensorFront1.distance * 100 
                distanceFront2 = sensorFront2.distance * 100

            
            

        #object is in front on the left half of the robot
        elif distanceFront2 > distanceFront1 + error and distanceFront1 + error < close:
            print("object detected on left side")


        # Case: object covers both front two sensors

        # left side
        elif distanceLeft > (distanceFront1/(math.sqrt(2)/2)) + error and distanceFront1 + error < close:
            print("object detected directly in front")

        # right side
        elif distanceRight > (distanceFront2/(math.sqrt(2)/2)) + error and distanceFront2 + error < close:
            print("object detected directly in front")

        
            

        


