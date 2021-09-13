from Pin_Declaration import *
avoid_count = 0

def obstacleCheck():
    
    distanceFront1 = distance(GPIO_ECHO_FRONT1)
    distanceFront2 = distance(GPIO_ECHO_FRONT2)   

    print("distanceFront1: ", distanceFront1, "distanceFront2", distanceFront2)

    if (distanceFront1 < tooClose and distanceFront1 > 5) or (distanceFront2 < tooClose and distanceFront2 > 5):
        print("\nobject detected? double checking...\n")
        pwm1.value = 0
        pwm2.value = 0    

        time.sleep(0.05)

        distanceFront1 = distance(GPIO_ECHO_FRONT1)
        distanceFront2 = distance(GPIO_ECHO_FRONT2)

        print("distanceFront1: ", distanceFront1, "distanceFront2", distanceFront2)

        # double check distances
        if (distanceFront1 < tooClose and distanceFront1 > 5) or (distanceFront2 < tooClose and distanceFront2 > 5):
            print("\nhmm, still not sure if theres an object there\n")

            time.sleep(0.05)

            distanceFront1 = distance(GPIO_ECHO_FRONT1)
            distanceFront2 = distance(GPIO_ECHO_FRONT2)

            print("distanceFront1: ", distanceFront1, "distanceFront2", distanceFront2)

            if (distanceFront1 < tooClose and distanceFront1 > 5) or (distanceFront2 < tooClose and distanceFront2 > 5):
                print("\nyep, theres an object there\n")
                return True

    print("nope, no object detected")
    return False



def reset(avoid_count):
    
    print("moving past obstacle...")

    pwm1.value = 1
    pwm2.value = 1

    # second straight
    time.sleep(1.8*avoid_count+4.5)

    print("turnig right...")

    # third turn
    turn(90)

    print("moving back to path...")
    pwm1.value = 1
    pwm2.value = 1

    # fourth straight 
    time.sleep(1.8*avoid_count)

    print("turning left to fix angle...")

    turn(-90)

    print("continuing....")

    pwm1.value = 1
    pwm2.value = 1



   

    

def avoid(avoid_count): 

    # first turn
    print("turning 90 degrees left...")
    turn(-90)

    print("moving forward a little")
    pwm1.value = 1
    pwm2.value = 1

    # second straight
    time.sleep(2.5)

    print("turning back")

    # second turn
    turn(90)
    avoid_count += 1
    return avoid_count

    

    


