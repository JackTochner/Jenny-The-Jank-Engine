import gpiozero
import datetime
import os
import time


import RPi.GPIO as GPIO
import time

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
    

#sensorFront2 = gpiozero.DistanceSensor(echo=24,trigger=5) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

#sensorFront1 = gpiozero.DistanceSensor(echo=23,trigger=6) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

#sensorLeft = gpiozero.DistanceSensor(echo=25,trigger=7) 

#sensorRight = gpiozero.DistanceSensor(echo=26,trigger=8) 

#define pwm values and output locations
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

# define the direction (this should be forward)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

#not sure if this works, but define which direction is forward
forward = direction1.value

#define encoder output
#encoder = gpiozero.RotaryEncoder(a=5, b=6,max_steps=100000) 

#error value means we may not be exactly aligned with the wall
error = 0.1

tooClose = 10

# create a new file based on date and time
now = datetime.datetime.now()
current_time = now.strftime("%d-%m %H-%M-%S")
file_name = "Jenny " + current_time 
#file_name_text = file_name + ".txt"
#nameOfFile = os.path.join("ECE3091 - Engineering Design/logs", file_name)



#f = open(file_name,"x")
f = open("output.txt","w")

def turn(degree):
    degPerSec = 35
    if degree < 0:
        degree = abs(degree)
        for i in range(round((degree/degPerSec)*10)):

            print("turning left")            
            pwm1.value = 0
            pwm2.value = 1            

            time.sleep(0.1)

    else:
        for i in range(round((degree/degPerSec)*10)):

            print("turning right")            
            pwm1.value = 1
            pwm2.value = 0

            time.sleep(0.1)


def output(string):
    print(string)
    string = string + "\n"
    f.write(string)

# def log_print(string,f):

#     f.write(string)
    
