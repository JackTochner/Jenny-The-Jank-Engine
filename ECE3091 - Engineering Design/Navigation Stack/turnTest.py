from Pin_Declaration import *
from obstacle_avoidance import *
import time

#straight1 = 640

straight1 = 37

# print("moving straight")
# for i in range(straight1):
    
#     pwm1.value = 1
#     pwm2.value = 1

    
#     while obstacleCheck():
#         print("obstacle found! avoiding...")
#         avoid()
#     time.sleep(0.01)

turn(-90)

for i in range(straight1):
    pwm1.value = 1
    pwm2.value = 1
    time.sleep(0.1)

pwm1.value = 0
pwm2.value = 0 