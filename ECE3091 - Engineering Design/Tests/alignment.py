import gpiozero
import time


sensorFront1 = gpiozero.DistanceSensor(echo=24,trigger=5) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

sensorFront2 = gpiozero.DistanceSensor(echo=23,trigger=6) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)


#left sensor and right sensor - wall alignment

#sensorRight = gpiozero.DistanceSensor(echo=24,trigger=7) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

#sensorLeft = gpiozero.DistanceSensor(echo=23,trigger=7) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

#define pwm values and output locations
pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)

# define the direction (this should be forward)
direction1 = gpiozero.OutputDevice(pin=4)
direction2 = gpiozero.OutputDevice(pin=27)

#not sure if this works, but define which direction is forward
forward = not direction1.value

#define encoder output
#encoder = gpiozero.RotaryEncoder(a=5, b=6,max_steps=100000) 

#error value means we may not be exactly aligned with the wall
error = 0.1

print('Entering While Loop...')

while True:
    distanceFront1 = sensorFront1.distance * 100 #mm to cm 
    distanceFront2 = sensorFront2.distance * 100  
    #distanceRight = sensorRight.distance / 100 
    #distanceLeft = sensorLeft.distance / 100 
    #maybe update to be in an array to save readings over time

    # print for testing
    print('Distance of front 1: ', distanceFront1)
    print('Distance of front 2: ', distanceFront2)
    #print('Distance of right: ', distanceRight)
    #print('Distance of left: ', distanceLeft)

    time.sleep(1)
    
    while (distanceFront1 > distanceFront2 + error or distanceFront1 < distanceFront2 - error):
        print('Aligning...')

        

        # update each direction to be pointing forward
        direction1.value = forward
        direction2.value = forward

        #print('Left Distance: ', distanceFront1)
        #print('Right Distance: ', distanceFront2)

        if  distanceFront1 > distanceFront2 + error:

            #assume that all (1) values are the left
            
            #spin left wheel forward
            pwm1.value = min(0.5,distanceFront1/distanceFront2)
            
            #spin right wheel backwards
            direction2.value = not direction1.value
            pwm2.value = pwm1.value
            

        elif distanceFront1 < distanceFront2 - error:

            #spin right wheel forwards
            pwm2.value = min(0.5,distanceFront2/distanceFront1)

            #spin left wheel backwards
            direction1.value = not direction2.value
            pwm1.value = pwm2.value

        distanceFront1 = sensorFront1.distance * 100 #mm to cm 
        distanceFront2 = sensorFront2.distance * 100  
        #distanceRight = sensorRight.distance / 100 
        #distanceLeft = sensorLeft.distance / 100 
        #maybe update to be in an array to save readings over time

        # print for testing
        print('Distance of front 1: ', distanceFront1)
        print('Distance of front 2: ', distanceFront2)
        #print('Distance of right: ', distanceRight)
        #print('Distance of left: ', distanceLeft)
        

        time.sleep(1)

        


print('Exiting While Loop...')
pwm1.value = 0
pwm2.value = 0

pwm1.off()
pwm2.off()
