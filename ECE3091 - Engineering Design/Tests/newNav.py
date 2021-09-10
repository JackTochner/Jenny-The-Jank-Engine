
import gpiozero
import time
import math



rotary1 = gpiozero.RotaryEncoder(23,24, max_steps=100000)
rotary2 = gpiozero.RotaryEncoder(5,6, max_steps=100000)

pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)
forward = direction1.value

direction1.value = forward
direction2.value = forward

stepsForFullTurn = 3650

def pwm_control(w_desired,w_measured,Kp,Ki,e_sum):
    
  duty_cycle = min(max(0,Kp*(w_desired-w_measured) + Ki*e_sum),1)
  e_sum = e_sum + w_desired-w_measured
  
  return duty_cycle, e_sum


def motor_simulator():
  pre_steps1=rotary1.steps
  pre_steps2=rotary2.steps
  time.sleep(0.01)
  
  angular1 = (2*math.pi*(rotary1.steps-pre_steps1))/(stepsForFullTurn*0.01)
  angular2 = (2*math.pi*(rotary2.steps-pre_steps2))/(stepsForFullTurn*0.01)
    
  return ((angular1+angular2)/2)
  
  
w = 0
w_desired = 2.0
w_measured = 0.0
duty_cycle = 0

e_sum = 0

for j in range(100):
    pwm1.value=duty_cycle
    pwm2.value=duty_cycle
    
    duty_cycle,e_sum = pwm_control(w_desired,w_measured,Kp=10.0,Ki=0.1,e_sum=e_sum)
    
    w_measured = motor_simulator()
    
    print(j, w_measured)
    print(j, w_desired)
    print(j, duty_cycle)
