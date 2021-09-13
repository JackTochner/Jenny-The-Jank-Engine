import RPi.GPIO as GPIO
import time

servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(1) # Initialization
print(1)
time.sleep(5)
print(2)
p.ChangeDutyCycle(2)
time.sleep(5)
print(3)
p.ChangeDutyCycle(3)
time.sleep(5)
print(4)
p.ChangeDutyCycle(4)
time.sleep(5)
print(5)
p.ChangeDutyCycle(5)
time.sleep(5)
print(6)
p.ChangeDutyCycle(6)
time.sleep(5)
print(7)
p.ChangeDutyCycle(7)
time.sleep(5)
print(8)
p.ChangeDutyCycle(8)
time.sleep(5)
print(9)
p.ChangeDutyCycle(9)
time.sleep(5)
print(10)
p.ChangeDutyCycle(10)
time.sleep(5)
