
# Ultrasonic sensor

# Hardware instructions
# VCC to 5v power on pi
# pi GND to breadboard GND bus then connect that to a rasp pi GND
# echo connects to breadboard 330 resistor and trigger to breadboard with 470 resistor
# the ends of the 330 resistor with the echo signal go to their respective gpios (1, 3, 24 and 23 as shown below)
# all four sensors use the same trigger but different gpio for echo - see below code
# the resistors form a voltage divider. 470 resistors go to breadboard GND 
# see schematic UStoPI.png in google drive

import gpiozero
import time


#two front sensors - distractor detection
# angle 15 degrees (need to detect distractors from afar?)

#sensorFront1 = gpiozero.DistanceSensor(echo=1,trigger=7) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

#sensorFront2 = gpiozero.DistanceSensor(echo=3,trigger=7) 
#echo connects to gpio 3 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)


#left sensor and right sensor - wall alignment

sensorRight = gpiozero.DistanceSensor(echo=24,trigger=7) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

sensorLeft = gpiozero.DistanceSensor(echo=23,trigger=7) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)
# distanceFront1 = 0 
# distanceFront2 = 0
# distanceRight = 0
# distanceLeft = 0

# changed to an infinite loop for j in range(10)
while True:
    
    #distanceFront1 = sensorFront1.distance / 100 #mm to cm 
    #distanceFront2 = sensorFront2.distance / 100  
    distanceRight = sensorRight.distance / 100 
    distanceLeft = sensorLeft.distance / 100 
    #maybe update to be in an array to save readings over time

    # print for testing
    #print('Distance of front 1: ', distanceFront1)
    #print('Distance of front 2: ', distanceFront2)
    print('Distance of right: ', distanceRight)
    print('Distance of left: ', distanceLeft)
    time.sleep(1)


# using the distance measurements

# left and right measurements - have the sensors placed higher so they see the walls
# and not the distractors

# front 1 and 2 might need to be angled or placed lower, 15 degrees - assuming thats the
# spread of the sensor - will only detect from a certain distance depending on sensor
# physical height (measure with protractor lol?)
# does 2cm to 400cm range accuracy to 3mm
