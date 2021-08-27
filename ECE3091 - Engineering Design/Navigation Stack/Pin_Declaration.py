import gpiozero
import datetime
import os


sensorFront1 = gpiozero.DistanceSensor(echo=24,trigger=5) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

sensorFront2 = gpiozero.DistanceSensor(echo=23,trigger=6) 
#echo connects to gpio 1 with 330 resistor and trigger to gpio 7 with 470 resistor
#other end of both resistors goes to gpio (? any)

#sensorLeft = gpiozero.DistanceSensor(echo=25,trigger=7) 

#sensorRight = gpiozero.DistanceSensor(echo=26,trigger=8) 

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


# create a new file based on date and time
now = datetime.datetime.now()
current_time = now.strftime("%d-%m %H-%M-%S")
file_name = "Jenny " + current_time 
#file_name_text = file_name + ".txt"
#nameOfFile = os.path.join("ECE3091 - Engineering Design/logs", file_name)



#f = open(file_name,"x")
f = open("placeholder.txt","w")

# def log_print(string,f):

#     f.write(string)
    
