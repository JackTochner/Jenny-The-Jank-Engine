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


    print("starting scuffed comp")

    # print("turning")

    # turn(-90)


    # print("turning finished, going straight")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    print("sleeping for 5 seconds")
    time.sleep(5)
    

    print("turning right")
    pwm1.value = 0
    pwm2.value = 0

    turn(-90)

    print("turn finished, going straight again")


    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    print("sleeping for 5 seconds")

    time.sleep(5)

    print("turning right")

    pwm1.value = 0
    pwm2.value = 0

    turn(-87)

    print("turn finished, going straight for a third time")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    print("sleeping for 5 seconds")

    time.sleep(5)

    print("turning right")

    pwm1.value = 0
    pwm2.value = 0

    turn(-87)

    print("turn finished, final straight now")

    direction1.value = forward
    direction2.value = forward

    pwm1.value = 1
    pwm2.value = 1

    print("sleeping for 5 seconds")

    time.sleep(5)

    print("Done!")
    pwm1.value = 0
    pwm2.value = 0






