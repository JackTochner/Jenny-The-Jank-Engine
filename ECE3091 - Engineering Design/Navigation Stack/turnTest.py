from Pin_Declaration import *
import time

straight1 = 37
turn = straight1 + 30
straight2 = turn + 30

for i in range(200):
    if i < straight1:
        print("here")
        pwm1.value = 1
        pwm2.value = 1

    elif i < turn:
        pwm2.value = 0

    elif i < straight1:
        pwm2.value = 1

    else:
        pwm1.value = 0
        pwm2.value = 0

    time.sleep(0.1)