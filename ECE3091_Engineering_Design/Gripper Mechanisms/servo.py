import RPi.GPIO as GPIO
import time

servoPIN = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)


p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(6.6) # Initialization
time.sleep(1)
p.ChangeDutyCycle(7.7)
time.sleep(1)
