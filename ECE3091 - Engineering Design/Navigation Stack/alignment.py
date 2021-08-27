import gpiozero
import time
from Pin_Declaration import *
import csv

def align():

    

    distanceFront1 = sensorFront1.distance * 100 
    distanceFront2 = sensorFront2.distance * 100 

    distanceFront1Array = [distanceFront1]
    distanceFront2Array = [distanceFront2]


    while (distanceFront1 > distanceFront2 + error or distanceFront1 < distanceFront2 - error):
        print('Aligning...')
        f.write('Aligning...\n')

        

        # update each direction to be pointing forward
        direction1.value = forward
        direction2.value = forward

        #print('Left Distance: ', distanceFront1)
        #print('Right Distance: ', distanceFront2)

        if  distanceFront1 > distanceFront2 + error:

            #assume that all (1) values are the left
            
            #spin left wheel forward
            pwm1.value = 0.5
            
            #spin right wheel backwards
            direction2.value = not direction1.value
            pwm2.value = pwm1.value
            

        elif distanceFront1 < distanceFront2 - error:

            #spin right wheel forwards
            pwm2.value = 0.5

            #spin left wheel backwards
            direction1.value = not direction2.value
            pwm1.value = pwm2.value

        distanceFront1 = sensorFront1.distance * 100 
        distanceFront2 = sensorFront2.distance * 100  

        distanceFront1Array.append(distanceFront1)
        distanceFront2Array.append(distanceFront2)


        #distanceRight = sensorRight.distance / 100 
        #distanceLeft = sensorLeft.distance / 100 
        #maybe update to be in an array to save readings over time

        # print for testing
        print('Distance of front 1: ', distanceFront1)
        f.write('Distance of front 1: \n', distanceFront1)

        print('Distance of front 2: ', distanceFront2)
        f.write('Distance of front 2: \n', distanceFront2)

        print('Direction1: ', direction1.value)
        f.write('Direction1: \n', direction1.value)

        print('Direction2: ', direction2.value)
        f.write('Direction2: \n', direction2.value)
        #print('Distance of right: ', distanceRight)
        #print('Distance of left: ', distanceLeft)
        

        time.sleep(0.1)

    


    print('Exiting While Loop...')
    f.write('Exiting While Loop...\n')
    pwm1.value = 0
    pwm2.value = 0

    pwm1.off()
    pwm2.off()

    print('Aligned!')
    f.write('Aligned!\n')

    file_name_csv = file_name + " align.csv"
    nameOfFile = os.path.join("ECE3091 - Engineering Design/logs", file_name_csv)
    f_csv = open(nameOfFile,"x")


    writer = csv.writer(f_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(distanceFront1Array)
    writer.writerow(distanceFront2Array)
