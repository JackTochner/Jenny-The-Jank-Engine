import gpiozero
import time
from Pin_Declaration import *
import csv

import RPi.GPIO as GPIO
#import time

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

def Align():    
    
    distanceFront1 = distance(GPIO_ECHO_FRONT1) 

    distanceFront2 = distance(GPIO_ECHO_FRONT2)

    distanceFront1Array = [distanceFront1]
    distanceFront2Array = [distanceFront2]

    pwm1.value = 0.5
    pwm2.value = 0.5


    while (distanceFront1 > distanceFront2 + error or distanceFront1 < distanceFront2 - error):
        output('Aligning...')             

        # update each direction to be pointing forward
        direction1.value = forward
        direction2.value = forward

        #print('Left Distance: ', distanceFront1)
        #print('Right Distance: ', distanceFront2)

        if  distanceFront1 > distanceFront2 + error:

            #assume that all (1) values are the left
            
            #spin left wheel forward
            
            
            #spin right wheel backwards
            #pwm2.value = pwm1.value
            direction2.value = not direction1.value
            
            

        elif distanceFront1 < distanceFront2 - error:

            #spin right wheel forwards
            

            #spin left wheel backwards
            #pwm1.value = pwm2.value
            direction1.value = not direction2.value
           
        
        time.sleep(0.1)
        distanceFront1 = distance(GPIO_ECHO_FRONT1) 
        time.sleep(0.1)
        distanceFront2 = distance(GPIO_ECHO_FRONT2)

        distanceFront1Array.append(distanceFront1)
        distanceFront2Array.append(distanceFront2)


        #distanceRight = sensorRight.distance / 100 
        #distanceLeft = sensorLeft.distance / 100 
        #maybe update to be in an array to save readings over time

        # print for testing
        
        string = 'Distance of front 1: ' + str(distanceFront1) 
        output(string)     
        
        string = 'Distance of front 2: ' + str(distanceFront2) 
        output(string)
        
        string = 'Direction1: ' + str(direction1.value) 
        output(string)
        
        string = 'Direction2: ' + str(direction2.value)
        output(string)
        #print('Distance of right: ', distanceRight)
        #print('Distance of left: ', distanceLeft)
        

        time.sleep(0.1)

    


    output('Exiting While Loop...')    
    pwm1.value = 0
    pwm2.value = 0

    pwm1.off()
    pwm2.off()

    output('Aligned!')
    
    #file_name_csv = file_name + " align.csv"
    #nameOfFile = os.path.join("ECE3091 - Engineering Design/logs", file_name_csv)
    
    
    f_align_csv = open("align.csv","w")    

    writer = csv.writer(f_align_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(distanceFront1Array)
    writer.writerow(distanceFront2Array)
    
Align()
