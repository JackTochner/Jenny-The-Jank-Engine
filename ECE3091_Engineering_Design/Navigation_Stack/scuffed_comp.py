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

                #print("turning right")            
                pwm1.value = 1
                pwm2.value = 1     

                direction1.value = not forward       

                time.sleep(0.1)

        else:
            for i in range(round((degree/degPerSec)*10)):

                #print("turning left")            
                pwm1.value = 1
                pwm2.value = 1

                direction2.value = not forward

                time.sleep(0.1)

        direction1.value = forward
        direction2.value = forward

    def driveToBall(x,y,w,h):

        direction1.value = forward
        direction2.value = forward

        
        x = x-600
        y = y-360

        #print("turning...")

        #print("turning ", (-x*45/600), " degrees")
        turn((-x*45/600)+5)

        pwm1.value = 0
        pwm2.value = 0

        #print("now facing ball. sleeping for 2 seconds...")
        #time.sleep(2)


        pwm1.value = 1
        pwm2.value = 1
        #print("moving forward for 20 seconds")

        i = 0
        while True:
            # if( i > 100 and i <105 ):

                
                
            #     direction1.value = not forward

            # else:
            #     direction1.value = forward

            # if i > 105:
            #     i = 0


            i += 1


    print("starting comp")

    # print("turning")

    # turn(-90)


    # print("turning finished, going straight")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1
    
    #print("sleeping for 10 seconds")
    for i in range(500):
        
        
        if foundObject[0]:
            print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])
        
        if( i > 100 and i <105 )or (i > 200 and i <205) or (i > 300 and i < 305) or (i>400 and i <405):
            #print("drift correction")
            direction1.value = not forward

        else:
            direction1.value = forward

        time.sleep(0.02)
            
    

    #print("turning right")
    pwm1.value = 0
    pwm2.value = 0

    print("first goal reached, moving to second")

    turn(-90)

    #print("turn finished, going straight again")


    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    #print("sleeping for 10 seconds")
    for i in range(500):
        
        if foundObject[0]:
            #print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])


        if( i > 100 and i <105 )or (i > 200 and i <205) or (i > 300 and i < 305) or (i>400 and i <405):
            #print("drift correction")
            direction1.value = not forward

        else:
            direction1.value = forward
            

        time.sleep(0.02)

    #print("turning right")

    pwm1.value = 0
    pwm2.value = 0

    print("second goal reached, moving to third")

    turn(-90)

    #print("turn finished, going straight for a third time")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    #print("sleeping for 10 seconds")
    for i in range(500):
        
        if foundObject[0]:
            #print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])

        if( i > 100 and i <105 )or (i > 200 and i <205) or (i > 300 and i < 305) or (i>400 and i <405):
            #print("drift correction")
            direction1.value = not forward

        else:
            direction1.value = forward
            

        time.sleep(0.02)

    #print("turning right")

    pwm1.value = 0
    pwm2.value = 0

    print("third goal reached, moving to fourth")

    turn(-90)

    #print("turn finished, final straight now")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    #print("sleeping for 10 seconds")
    for i in range(500):
        
        if foundObject[0]:
            #print("Object Found!!!")
            driveToBall(foundObject[1],foundObject[2],foundObject[3],foundObject[4])

        if( i > 100 and i <105 )or (i > 200 and i <205) or (i > 300 and i < 305) or (i>400 and i <405):
            #print("drift correction")
            direction1.value = not forward

        else:
            direction1.value = forward
            

        time.sleep(0.02)

    print("All positions reached, no bearing found")
    pwm1.value = 0
    pwm2.value = 0






