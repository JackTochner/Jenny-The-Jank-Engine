from Pin_Declaration import *
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%d-%m %H-%M")

file_name = "Jenny " + current_time

f = open(file_name,"x")

f = open(file_name,"w")


direction1 = not direction1

pwm1.value = 0.5
pwm2.value = 0.5

f.write(sensorFront1,sensorFront2,sensorLeft,sensorRight)

#f.write("test")
f.close()

