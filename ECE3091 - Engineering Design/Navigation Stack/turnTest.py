from Pin_Declaration import *
from obstacle_avoidance import *
import time
import math

#straight1 = 518

x = 30
y = 30

#straight1 = 37

def goal(x,y):
    

    distance = math.sqrt(x**2+y**2)

    angle = math.degrees(math.atan(x/y))

    return angle, distance

angle, xydistance = goal(x,y)

print("angle: ", angle, "xydistance", xydistance)

straight1 = (xydistance*10)*(37/30)

print('looking at goal...')

turn(angle)

print("moving straight")

i = 0
found = False
while i <straight1:
    
    pwm1.value = 1
    pwm2.value = 1

    avoid_count = 0
    
    if not found:
        while obstacleCheck():
            print("obstacle found! avoiding...")
            found = True
            avoid_count = avoid(avoid_count)

            reset(avoid_count)

            straight1 = straight1-((1.8*avoid_count+4.5)*100)

    #print("i", i, "straight1" , straight1)

    # if found:
    #     print("i", i, "straight1" , straight1)
    #     break

    i = i+1
    time.sleep(0.01)

print("i", i, "straight1" , straight1)
pwm1.value = 0
pwm2.value = 0 

time.sleep(1)

turn(-45)
# for i in range(straight1):
#     pwm1.value = 1
#     pwm2.value = 1
#     time.sleep(0.1)

# turn(-90)

# for i in range(straight1):
#     pwm1.value = 1
#     pwm2.value = 1
#     time.sleep(0.1)

pwm1.value = 0
pwm2.value = 0 