import gpiozero
import datetime
import os
import time
import RPi.GPIO as GPIO
import sys
import csv

#GPIO Mode (BOARD / BCM - refer to pins)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 26
GPIO_ECHO_FRONT = 25
GPIO_ECHO_LEFT = 22
#GPIO_ECHO_LEFT = 1
GPIO_ECHO_RIGHT = 18

#free # 17,22,16



#occ # 4,27,13,6,5,12,23,24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN)
GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN)
GPIO.setup(GPIO_ECHO_FRONT, GPIO.IN)
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

error = 0.01

tooClose = 30

# create a new file based on date and time
now = datetime.datetime.now()
current_time = now.strftime("%d-%m %H-%M-%S")
file_name = "Jenny " + current_time 

create_new_file = False

#path = "Jenny-The-Jank-Engine/ECE3091\ -\ Engineering\ Design/Navigation\ Stack/"

if create_new_file:

    file_name_text = file_name + ".txt"
    nameOfFile = os.path.join("/home/pi/Jenny-The-Jank-Engine/ECE3091_Engineering_Design/logs", file_name_text)
    f = open(nameOfFile,"x")   


else:
    f = open("/home/pi/Jenny-The-Jank-Engine/ECE3091_Engineering_Design/logs/output.txt","w")

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
    string = str(string)
    print(string)
    string = string + "\n"
    f.write(string)


def csvFileCreater(name, newFile=False):
    if newFile:
        name = name + ".csv"
        nameOfFile = os.path.join("/home/pi/Jenny-The-Jank-Engine/ECE3091_Engineering_Design/logs", file_name_text)
        f = open(nameOfFile,"x")  

    else:

        f = open("/home/pi/Jenny-The-Jank-Engine/ECE3091_Engineering_Design/logs/"+name+".csv","w")

    return f

def outputcsv(file,number):
        writer = csv.writer(file)
        #string = str(string)
        #print(number)
        #string = string + "\n"
        writer.writerow(number)
