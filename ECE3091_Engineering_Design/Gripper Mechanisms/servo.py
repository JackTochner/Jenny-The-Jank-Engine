import RPi.GPIO as GPIO
import time

servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(1) # Initialization
time.sleep(5)
p.ChangeDutyCycle(2)
time.sleep(5)
p.ChangeDutyCycle(3)
time.sleep(5)
p.ChangeDutyCycle(4)
time.sleep(5)
p.ChangeDutyCycle(5)
time.sleep(5)
p.ChangeDutyCycle(6)
time.sleep(5)
p.ChangeDutyCycle(7)
time.sleep(5)
p.ChangeDutyCycle(8)
time.sleep(5)
p.ChangeDutyCycle(9)
time.sleep(5)
p.ChangeDutyCycle(10)
time.sleep(5)
