#f = open("C:\\Users\\jackb\\OneDrive\\Documents\\GitHub\\Jenny-The-Jank-Engine\\ECE3091_Engineering_Design\\Navigation_Stack\\output.txt","w")
#/home/pi/Jenny-The-Jank-Engine/

f = open("/home/pi/Jenny-The-Jank-Engine/ECE3091_Engineering_Design/Navigation_Stack/output.txt","w")

def output(string):
    print(string)
    string = string + "\n"
    f.write(string)


