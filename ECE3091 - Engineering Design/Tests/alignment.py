import gpiozero
import time
from UltrasonicSensor import *

pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)
encoder = gpiozero.RotaryEncoder(a=5, b=6,max_steps=100000) 

error = 0.1

while (distanceFront1 > distanceFront2 + error or distanceFront1 < distanceFront2 - error):
    if  distanceFront1 > distanceFront2 + error:

        #assume that all (1) values are the left
        pwm2.value = 0
        pwm1.value = min(0.5,distanceFront1/distanceFront2)
        

    elif distanceFront1 < distanceFront2 - error:

        pwm1.value = 0
        pwm2.value = min(0.5,distanceFront2/distanceFront1)

    time.sleep(1)

pwm1.value = 0
pwm2.value = 0