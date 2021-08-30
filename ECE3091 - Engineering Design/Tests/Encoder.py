import gpiozero
import time

rotary1 = gpiozero.RotaryEncoder(5,6,max_steps=32)
rotary2 = gpiozero.RotaryEncoder(23,24,max_steps=32)
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

forward = not direction1.value

pre_steps = 0

pwm1.value = 1
pwm2.value = 1

time.sleep(5.0)

print('Counter:',encoder.steps,'Speed:',(encoder.steps-pre_steps)/5.0,'steps per second\n')
pre_steps = encoder.steps
