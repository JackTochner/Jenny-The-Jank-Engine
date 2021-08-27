#from Pin_Declaration import *
import os
from datetime import datetime
import matplotlib.pyplot as plt
import csv

# now = datetime.now()

# current_time = now.strftime("%d-%m %H-%M-%S")

# file_name = "Jenny " + current_time +".txt"

# nameOfFile = os.path.join("ECE3091 - Engineering Design/logs", file_name)

# f = open(nameOfFile,"x")
# f.write('test\n')
# f.write('test\n')

# num = 2561


# f.close()

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
f = open("test.csv","w")

writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

writer.writerow(x)
writer.writerow(y)

