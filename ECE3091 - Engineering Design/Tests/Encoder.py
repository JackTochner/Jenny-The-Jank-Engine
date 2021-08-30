import gpiozero
import time

rotary1 = gpiozero.RotaryEncoder(5,6, max_steps=100000)
rotary2 = gpiozero.RotaryEncoder(23,24, max_steps=100000)
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

forward = not direction1.value

pre_steps = 0

pwm1.value = 0.5
pwm2.value = 0.5

f = open('encoderLog.txt','w')

pre_steps1=0
pre_steps2=0

while True:
    string = 'Counter: ' + str(rotary1.steps) + '\tSpeed: ' + str((rotary1.steps-pre_steps1)/0.2) + 'steps per second'

    print("rotary1:\n\n")
    print(string)
    string = string + "\n"
    f.write(string)

    string = 'Counter: ' + str(rotary2.steps) + '\tSpeed: ' + str((rotary2.steps-pre_steps2)/0.2) + 'steps per second'

    print('rotary2:\n\n')
    print(string)
    string = string + "\n"
    f.write(string)

    pre_steps1 = rotary1.steps
    pre_steps2 = rotary2.steps

    time.sleep(1)
