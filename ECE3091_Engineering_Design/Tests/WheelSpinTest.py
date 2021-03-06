
import gpiozero
import time
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)
encoder = gpiozero.RotaryEncoder(a=5, b=6,max_steps=100000) 
# This class has a lot more functionality,so worth reading up on it
# Step through duty cycle values, slowly increasing the speed and changing the direction of motion
direction1.value = not direction1.value
direction2.value = not direction2.value
pre_steps = 0
for j in range(2):
    pwm1.value = 0
    pwm2.value = 1
    print('Duty cycle:',pwm1.value,'Direction:',direction1.value)
    time.sleep(5.0)
    print('Counter:',encoder.steps,'Speed:',(encoder.steps-pre_steps)/5.0,'steps per second\n')
    pre_steps = encoder.steps
    
    #NB, if steps keeps increasing, what about integer overflows?

pwm1.off()
pwm2.off()
