import sys
import picamera
import time
sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")
from ECE3091_Engineering_Design.Navigation_Stack.Pin_Declaration import *
from ECE3091_Engineering_Design.Navigation_Stack.Navigation import *
from ECE3091_Engineering_Design.Navigation_Stack.ImageNavigation import *

while distance(GPIO_ECHO_FRONT1) > 0.3:
    pwm1.value = 1
    pwm2.value = 2



camera = picamera.PiCamera()

camera.capture("NNPic.jpg")

#time.delay(1)


