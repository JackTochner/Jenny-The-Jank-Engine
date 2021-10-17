from Pin_Declaration import *



def scuffed_comp_func(foundObject):


    direction1 = gpiozero.OutputDevice(pin=4)
    direction2 = gpiozero.OutputDevice(pin=27)
        
    pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000) #Right
    pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000) #Left

    forward = not direction1.value

    direction1.value = forward
    direction2.value = forward


    def turn(degree):
        degPerSec = 62
        if degree < 0:
            degree = abs(degree)
            for i in range(round((degree/degPerSec)*10)):

                print("turning right")            
                pwm1.value = 1
                pwm2.value = 1     

                direction1.value = not forward       

                time.sleep(0.1)

        else:
            for i in range(round((degree/degPerSec)*10)):

                print("turning left")            
                pwm1.value = 1
                pwm2.value = 1

                direction2.value = not forward

                time.sleep(0.1)

        direction1.value = forward
        direction2.value = forward

    def driveToBall(x,y,w,h):

        
        x = x-600
        y = y-360

        print("turning...")

        print("turning ", (-x*45/600), " degrees")
        turn((-x*55/600))

        pwm1.value = 0
        pwm2.value = 0

        print("now facing ball. sleeping for 2 seconds...")
        #time.sleep(2)


        pwm1.value = 1
        pwm2.value = 1
        print("moving forward for 20 seconds")

        i = 0
        while True:
            if( i > 100 and i <107 ):
                i = 0
                direction1.value = not forward

            else:
                direction1.value = forward


            i += 1


    print("starting scuffed comp")

    # print("turning")

    # turn(-90)


    # print("turning finished, going straight")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1
    
    print("sleeping for 10 seconds")
    for i in range(500):
        
        
        if foundObject[0]:
            print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])
        
        if( i > 100 and i <107 )or (i > 200 and i <207) or (i > 300 and i < 307) or (i>400 and i <407):
            direction1.value = not forward

        else:
            direction1.value = forward

        time.sleep(0.02)
            
    

    print("turning right")
    pwm1.value = 0
    pwm2.value = 0

    turn(-90)

    print("turn finished, going straight again")


    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    print("sleeping for 10 seconds")
    for i in range(500):
        
        if foundObject[0]:
            print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])


        if( i > 100 and i <107 )or (i > 200 and i <207) or (i > 300 and i < 307) or (i>400 and i <407):
            direction1.value = not forward

        else:
            direction1.value = forward
            

        time.sleep(0.02)

    print("turning right")

    pwm1.value = 0
    pwm2.value = 0

    turn(-90)

    print("turn finished, going straight for a third time")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    print("sleeping for 10 seconds")
    for i in range(500):
        
        if foundObject[0]:
            print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])
            

        time.sleep(0.02)

    print("turning right")

    pwm1.value = 0
    pwm2.value = 0

    turn(-90)

    print("turn finished, final straight now")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    print("sleeping for 10 seconds")
    for i in range(500):
        
        if foundObject[0]:
            print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])
            

        time.sleep(0.02)

    print("Done!")
    pwm1.value = 0
    pwm2.value = 0






