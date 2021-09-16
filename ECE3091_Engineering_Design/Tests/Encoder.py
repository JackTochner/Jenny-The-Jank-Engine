import gpiozero
import time
import math

rotary1 = gpiozero.RotaryEncoder(23,24, max_steps=100000)
rotary2 = gpiozero.RotaryEncoder(5,6, max_steps=100000)
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

forward = not direction1.value

pwm1.value = 1
pwm2.value = 1


pre_steps1=0
pre_steps2=0

maxSteps = 3650

wheelRadius = 0.026

while True:
    print(rotary1.steps)
    
    angular1 = (2*math.pi*(rotary1.steps-pre_steps1))/(maxSteps*5)
    velocity1 = angular1*wheelRadius
    
    string = 'Counter: ' + str(rotary1.steps) + '\tSpeed: ' + str((rotary1.steps-pre_steps1)/5) + 'steps per second' + '\tAngularVel: ' + str(angular1) + 'Linear V: ' + str(velocity1)

    print("rotary1:\n\n")
    print(string)
    string = string + "\n"


    angular2 = (2*math.pi*(rotary1.steps-pre_steps1))/(maxSteps*5)
    velocity2 = angular2*wheelRadius
    
    string = 'Counter: ' + str(rotary2.steps) + '\tSpeed: ' + str((rotary2.steps-pre_steps2)/5) + 'steps per second'+ '\tAngularVel: ' + str(angular2) + 'Linear V: ' + str(velocity1)

    print('rotary2:\n\n')
    print(string)
    string = string + "\n"
    
    print("Average velocity: " + str((velocity1+velocity2)/2) + "Distance Travelled" + str((velocity1+velocity2)/2*5.0))
    
    pre_steps1 = rotary1.steps
    pre_steps2 = rotary2.steps

    time.sleep(5)
