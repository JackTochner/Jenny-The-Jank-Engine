from alignment import align
from obstacle_avoidance import obstacle_avoid
import gpiozero
import time


import gpiozero

sensorFront1 = gpiozero.DistanceSensor(echo=23,trigger=5) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

sensorFront2 = gpiozero.DistanceSensor(echo=24,trigger=6) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

sensorSide1 = gpiozero.DistanceSensor(echo=25,trigger=7) 

sensorSide2 = gpiozero.DistanceSensor(echo=26,trigger=8) 

#define pwm values and output locations
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

# define the direction (this should be forward)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

#not sure if this works, but define which direction is forward
forward = not direction1.value

#define encoder output
#encoder = gpiozero.RotaryEncoder(a=5, b=6,max_steps=100000) 

#error value means we may not be exactly aligned with the wall
error = 0.1

distanceFront1 = sensorFront1.distance * 100 #mm to cm 
distanceFront2 = sensorFront2.distance * 100  
#distanceRight = sensorRight.distance / 100 
#distanceLeft = sensorLeft.distance / 100 
#maybe update to be in an array to save readings over time

# print for testing
print('Distance of front 1: ', distanceFront1)
print('Distance of front 2: ', distanceFront2)
#print('Distance of right: ', distanceRight)
#print('Distance of left: ', distanceLeft)

align()