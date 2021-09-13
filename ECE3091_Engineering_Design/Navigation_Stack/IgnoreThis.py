import datetime
import os

now = datetime.datetime.now()
current_time = now.strftime("%d-%m %H-%M-%S")
file_name = "Jenny " + current_time 

create_new_file = True

if create_new_file:

    file_name_text = file_name + ".txt"
    nameOfFile = os.path.join("/home/pi/Jenny-The-Jank-Engine/ECE3091_Engineering_Design", file_name_text)
    print(nameOfFile)
    f = open(nameOfFile,"x")   

#f = open("C:\\Users\\jackb\\OneDrive\\Documents\\GitHub\\Jenny-The-Jank-Engine\\ECE3091_Engineering_Design\\Navigation_Stack\\output2.txt","x")

#/home/pi/Jenny-The-Jank-Engine/



#f = open("/home/pi/Jenny-The-Jank-Engine/ECE3091_Engineering_Design/Navigation_Stack/output2.txt","x")

def output(string):
    print(string)
    string = string + "\n"
    f.write(string)


