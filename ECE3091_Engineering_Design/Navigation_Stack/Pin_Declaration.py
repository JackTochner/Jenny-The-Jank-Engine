import gpiozero
import datetime
import os
import time
import RPi.GPIO as GPIO
import sys


#GPIO Mode (BOARD / BCM - refer to pins)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 26
GPIO_ECHO_FRONT1 = 25
GPIO_ECHO_FRONT2 = 22
#GPIO_ECHO_LEFT = 1
#GPIO_ECHO_RIGHT = 3


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO_FRONT1, GPIO.IN)
GPIO.setup(GPIO_ECHO_FRONT2, GPIO.IN)
#GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN)
#GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN)


def distance(gpio_echo):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(gpio_echo) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(gpio_echo) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    dist = (TimeElapsed * 34300) / 2

    return dist
    
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

# define the direction (this should be forward)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

forward = direction1.value

error = 0.1

tooClose = 18

# create a new file based on date and time
now = datetime.datetime.now()
current_time = now.strftime("%d-%m %H-%M-%S")
file_name = "Jenny " + current_time 

create_new_file = False

#path = "Jenny-The-Jank-Engine/ECE3091\ -\ Engineering\ Design/Navigation\ Stack/"

if create_new_file:

    file_name_text = file_name + ".txt"
    nameOfFile = os.path.join("Jenny-The-Jank-Engine/ECE3091-Engineering-Design/logs", file_name)
    f = open(file_name,"x")   


else:
    f = open("output.txt","w")

def turn(degree):
    degPerSec = 71
    if degree < 0:
        degree = abs(degree)
        for i in range(round((degree/degPerSec)*10)):

            print("turning left")            
            pwm1.value = 1
            pwm2.value = 1     

            direction1.value = not forward       

            time.sleep(0.1)

    else:
        for i in range(round((degree/degPerSec)*10)):

            print("turning right")            
            pwm1.value = 1
            pwm2.value = 1

            direction2.value = not forward

            time.sleep(0.1)

    direction1.value = forward
    direction2.value = forward


def output(string):
    print(string)
    string = string + "\n"
    f.write(string)

# def log_print(string,f):

#     f.write(string)
    
