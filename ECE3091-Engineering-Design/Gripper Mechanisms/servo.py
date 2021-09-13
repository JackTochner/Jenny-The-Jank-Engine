import RPi.GPIO as GPIO
import time

servo_pin = 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

# set the frequency of the servo's pwm
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# input values are percentages of the duty cycle that turn the servo different directions and amounts
pwm.ChangeDutyCycle(5) # left -90 deg position
sleep(1)
pwm.ChangeDutyCycle(7.5) # neutral position
sleep(1)
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(1)

# neutral location - 0 degrees - 1500us = 1.5ms = 0.0015s

pwm.stop()
GPIO.cleanup()

def setAngle(angle):
    duty_cycle = #ratio relationship
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(duty)
