import RPi.GPIO as GPIO
import time

servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(10) # Initialization
time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
