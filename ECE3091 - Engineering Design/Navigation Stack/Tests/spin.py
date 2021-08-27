#from Pin_Declaration import *
import os
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%d-%m %H-%M-%S")

file_name = "Jenny " + current_time +".txt"

nameOfFile = os.path.join("ECE3091 - Engineering Design/logs", file_name)

f = open(nameOfFile,"x")
f.write('test\n')
f.write('test\n')

num = 2561


f.close()

