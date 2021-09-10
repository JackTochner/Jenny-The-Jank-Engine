
import gpiozero
import datetime
import os
import time


import RPi.GPIO as GPIO
import time


pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

# define the direction (this should be forward)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

#not sure if this works, but define which direction is forward
forward = direction1.value

counter = 0
while (counter<1):
  pwm1.value=1
  pwm2.value=1

