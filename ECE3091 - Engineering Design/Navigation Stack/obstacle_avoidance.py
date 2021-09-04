from Pin_Declaration import *
# import math



# def obstacle_avoid():

#     #ASSUMPTIONS:
#     # - robot is aligned before obstacle avoidance starts
#     # - any object is large enough such that, if the object is in front of the robot, and within the close value, at least one of the sensors will detect it

#     obstacle_distance = None

#     while True:

#         distanceRight = sensorRight.distance * 100 
#         distanceLeft = sensorLeft.distance * 100
#         distanceFront1 = sensorFront1.distance * 100 
#         distanceFront2 = sensorFront2.distance * 100 

#         # move forward
#         pwm1.value = 0.5
#         pwm2.value = 0.5      


#         # Detect Objects in relation to Robot
#         output("trying to detect objects...")        


#         # Case: about to hit a wall
#         if distanceFront1 + error < 3 and distanceFront2 + error < 3 and distanceLeft + error< 3/(math.sqrt(2)/2) and distanceRight + error < 3/(math.sqrt(2)/2):
#             output("wall found. stopping...")            
#             pwm1.value = 0
#             pwm2.value = 0
#             break

#         # Case: object only covering one front sensor

#         #object is in front on the right half of the robot

        
#         #elif distanceFront1 > distanceFront2 + error and distanceFront2+error < close: 
#         elif compare(distanceFront1,distanceFront2):
#             output("object detected on right side")            
         
#             avoid(sensorFront1,sensorFront2,not direction1, direction2)

#             # while distanceFront1 > distanceFront2 + error and distanceFront2+error < close:
#             #     direction1 = not direction1

#             #     distanceFront1 = sensorFront1.distance * 100 
#             #     distanceFront2 = sensorFront2.distance * 100

            
            

#         #object is in front on the left half of the robot
#         #elif distanceFront2 > distanceFront1 + error and distanceFront1 + error < close:

#         elif compare(distanceFront2,distanceFront1):
#             output("object detected on left side")           
#             avoid(sensorFront2,sensorFront1, direction1, not direction2)


#         # Case: object covers both front two sensors

#         # left side
#         #elif distanceLeft > (distanceFront1/(math.sqrt(2)/2)) + error and distanceFront1 + error < close:
#         elif compare(distanceLeft,distanceFront1,math.sqrt(2)/2):
#             output("object detected directly in front (1)")            
#             avoid(sensorLeft,sensorFront1, direction1, not direction2)

#         # right side
#         #elif distanceRight > (distanceFront2/(math.sqrt(2)/2)) + error and distanceFront2 + error < close:
#         elif compare(distanceRight,distanceFront2,math.sqrt(2)/2):
#             output("object detected directly in front (2)")            
#             avoid(sensorRight,sensorFront2,not direction1, direction2)

        
# def compare(x,y,math=1):
#     # Variable used to define how close an object will need to be before the robot will turn away
#     close = 10
#     return x>((y/math)+error) and y + error < close

        
# def avoid(x,y,new_direction1,new_direction2, math = 1):
#         output("avoiding...")        
#         direction1.value = new_direction1
#         direction2.value = new_direction2

#         obstacle_distance = y.distance
       
#         string = "object is " + obstacle_distance.str() + " cm away"
#         output(string)

#         while compare(x.distance*100,y.distance*100,math):  
#             output("still avoiding...")            
#             print(x.distance*100)
#             print(y.distance*100)      


            
#         output("avoided!")        
#         output("moving forward...")
       
#         direction1.value = forward
#         direction2.value = forward

def obstacleCheck():
    distanceFront1 = distance(GPIO_ECHO_FRONT1)
    distanceFront2 = distance(GPIO_ECHO_FRONT2)

    print("distanceFront1: ", distanceFront1, "distanceFront2", distanceFront2)

    if distanceFront1 < tooClose or distanceFront2 < tooClose:
        print("object detected? double checking...")
        pwm1.value = 0
        pwm2.value = 0    

        time.sleep(0.1)

        distanceFront1 = distance(GPIO_ECHO_FRONT1)
        distanceFront2 = distance(GPIO_ECHO_FRONT2)

        print("distanceFront1: ", distanceFront1, "distanceFront2", distanceFront2)

        # double check distances
        if distanceFront1 < tooClose or distanceFront2 < tooClose:
            print("yep, theres an object there")
            return True

    print("nope, no object detected")
    return False



def avoid():
    
    print("turning 90 degrees right...")
    turn(-90)

    print("moving forward a little")
    pwm1.value = 1
    pwm2.value = 1

    time.sleep(1)

    print("turning back")
    turn(90)

    

    


