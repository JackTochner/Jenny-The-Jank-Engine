import RPi.GPIO as GPIO
import time

servo_pin = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

# set the frequency of the servo's pwm
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# input values are percentages of the duty cycle that turn the servo different directions and amounts
for i in range(60):
    pwm.ChangeDutyCycle(7.5) # not sure how far this will turn - 90 degrees from neutral
    sleep(0.1)


# neutral location - 0 degrees - 1500us = 1.5ms = 0.0015s
# 50Hz * 0.0015s = 0.075 of a cycle. 7.5% duty cycle is neutral
# 2.5% is -180, 5% is -90, 7.5% is 0, 10% is 90, 12.5% is 180

pwm.stop()
GPIO.cleanup()

# def setAngle(angle):
#     duty_cycle = #ratio relationship
#     GPIO.output(servo_pin, True)
#     pwm.ChangeDutyCycle(duty)
#     sleep(1)
#     GPIO.output(servo_pin, False)
#     pwm.ChangeDutyCycle(duty)
