import gpiozero
import datetime
import os
import time
import RPi.GPIO as GPIO
import sys
import csv

from multiprocessing import Process, Manager


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

def distance(distances,obstacleDetected):

    #dists = [500,500,500]

 
    gpio_echo = [GPIO_ECHO_LEFT,GPIO_ECHO_FRONT,GPIO_ECHO_RIGHT]

    obstacle = [0,0,0]

    #obstacleDetected = [False,False,False]

    while True:

        for i in range(3):
            # pwm1Save = pwm1.value
            # pwm2Save = pwm2.value

            # pwm1.value = 0
            # pwm2.value = 0
            # set Trigger to HIGH
            GPIO.output(GPIO_TRIGGER, True)

            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER, False)

            loopStartTime = time.time()

            StartTime = time.time()
            StopTime = time.time()

            # save StartTime
            while GPIO.input(gpio_echo[i]) == 0:
                StartTime = time.time()
                if StartTime - loopStartTime > 0.005:
                    return 100
                

            #print("GPIO = 0: ",loopStartTime-StartTime)

            # save time of arrival
            while GPIO.input(gpio_echo[i]) == 1:
                StopTime = time.time()
                if (StopTime - StartTime)>=0.01:
                    break
            #print("GPIO = 1: ",StartTime - StopTime, "\n")
            # time difference between start and arrival
            TimeElapsed = StopTime - StartTime
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distances[i] = (TimeElapsed * 34300) / 2
            #dists.append(dist)
            # pwm1.value = pwm1Save
            # pwm2.value = pwm2Save

            if distances[i] < tooClose:

                if obstacle[i] <8:
                    obstacle[i] = obstacle[i]+1

                if obstacle[i] >= 3:
                    obstacleDetected[i] = True
                

            else:

                if obstacle[i] > 0:
                    obstacle[i] = obstacle[i] -1

                if obstacle[i] < 3:                   
                    obstacleDetected[i] = False

                
            #print((TimeElapsed * 34300) / 2)
            # print("\n")
            # print(obstacle)
            # print(obstacleDetected)
            # print("\n")

        time.sleep(0.02)

    #return distances


    
# pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000) #Right
# pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000) #Left

# pwm1.value = 1
# pwm2.value = 1

# define the direction (this should be forward)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

forward = direction1.value

error = 0.01

tooClose = 15

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
