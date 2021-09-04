from Pin_Declaration import *
from obstacle_avoidance import *
import time

straight1 = 640

#straight1 = 37

print("moving straight")
for i in range(straight1):
    
    pwm1.value = 1
    pwm2.value = 1

    avoid_count = 0
    print("here")
    while obstacleCheck():
        print("obstacle found! avoiding...")
        avoid_count = avoid(avoid_count)

        reset(avoid_count)
    time.sleep(0.01)

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