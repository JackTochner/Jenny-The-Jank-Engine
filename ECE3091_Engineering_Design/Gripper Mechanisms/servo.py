import RPi.GPIO as GPIO
import time

servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(6) # Initialization
print(6)
time.sleep(5)
print(6.5)
p.ChangeDutyCycle(6.5)
time.sleep(5)
print(7)
p.ChangeDutyCycle(7)
time.sleep(5)
print(7.5)
p.ChangeDutyCycle(7.5)
time.sleep(5)
print(8)
p.ChangeDutyCycle(8)
time.sleep(5)
