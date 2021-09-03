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

# function calls in an infinite loop...???

var = None
i = 0
while True: 
    #distanceFront1 = distance(GPIO_ECHO_FRONT1)
    if i == 0:
        var = GPIO_ECHO_FRONT1
        i =1
    elif i == 1:
        var = GPIO_ECHO_FRONT2
        i = 0
    
    distanceFront2 = distance(var)
    # distanceFront1 = distance(GPIO_ECHO_FRONT1)
    # time.sleep(1)
    # distanceFront2 = distance(GPIO_ECHO_FRONT2)
    # time.sleep(1)
    #distanceLeft = distance(GPIO_ECHO_LEFT)
    #distanceRight = distance(GPIO_ECHO_RIGHT)

    #print('Distance of front 1: ', distanceFront1)
    print('Distance of front 2: ', distanceFront2)
    #print('Distance of right: ', distanceLeft)
    #print('Distance of left: ', distanceRight)

# not really sure if cleanup is relevant - clears resources
#and resets pins (can enter pins as argument)
GPIO.cleanup()
