import gpiozero
import time

#import and run the UltrasonicSensor file to continuously get sensor input
from UltrasonicSensor import *

#define pwm values and output locations
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

# define the direction (this should be forward)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

#not sure if this works, but define which direction is forward
forward1 = direction1.value
forward2 = direction2.value

#define encoder output
encoder = gpiozero.RotaryEncoder(a=5, b=6,max_steps=100000) 

#error value means we may not be exactly aligned with the wall
error = 0.1

while (distanceFront1 > distanceFront2 + error or distanceFront1 < distanceFront2 - error):

    # update each direction to be pointing forward
    direction1.value = forward1
    direction2.value = forward2

    if  distanceFront1 > distanceFront2 + error:

        #assume that all (1) values are the left
        
        #spin left wheel forward
        pwm1.value = min(0.5,distanceFront1/distanceFront2)\
        
        #spin right wheel backwards
        direction2.value = not direction1.value
        pwm2.value = pwm1.value
        

    elif distanceFront1 < distanceFront2 - error:

        #spin right wheel forwards
        pwm2.value = min(0.5,distanceFront2/distanceFront1)

        #spin left wheel backwards
        direction1.value = not direction2.value
        pwm1.value = pwm2.value

    time.sleep(1)

pwm1.value = 0
pwm2.value = 0

pwm1.off()
pwm2.off()