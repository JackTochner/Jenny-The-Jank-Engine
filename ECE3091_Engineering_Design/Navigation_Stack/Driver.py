import os
from datetime import datetime
import sys
#from ECE3091_Engineering_Design.Object_Detection import im_detect

#print("here1")

sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")
#from ECE3091_Engineering_Design.Navigation_Stack.Alignment import *
#from Pin_Declaration import *
#from Mapping import *
#from Alignment import Align

# need to check if importing only the function will work...

#from Navigation_Main import *

from im_detect import *
from newNav import *

#from SearchMode import *




# def turn(degree):
#     degPerSec = 63
#     if degree < 0:
#         degree = abs(degree)
#         for i in range(round((degree/degPerSec)*10)):

#             print("turning left")            
#             pwm1.value = 1
#             pwm2.value = 1     

#             direction1.value = not forward       

#             time.sleep(0.1)

#     else:
#         for i in range(round((degree/degPerSec)*10)):

#             print("turning right")            
#             pwm1.value = 1
#             pwm2.value = 1

#             direction2.value = not forward

#             time.sleep(0.1)

#     direction1.value = forward
#     direction2.value = forward
#camera = PiCamera()  

def main(align = False, navigate = False, comp=True, scuffed_comp = False):
   
    #print("here")

    if navigate:
        #output("Starting Navigation")

        Navigate(0,0,-math.pi)

        #output("Finished Navigation")

    if comp:
        #output("Starting Search...")   
        # 
            


            with Manager() as manager:

                print("starting navigation...")

                distances = manager.list([500,500,500])
                obstacleDetected = manager.list([False,False,False])

                foundObject = manager.list([0,0,0,0,0])

                ########################################################################################
                # Nav 1
                ########################################################################################

                # print("turning...")

                # #turn(-90)
                # print("not actually turning lol")

                # print("finished turning")

                

                time.sleep(2)

                US = Process(target = distance, args = (distances,obstacleDetected))

                #nav = Process(target = Navigate, args = (0.6,0,0,distances,obstacleDetected,foundObject))  
                nav = Process(target = Navigate, args = (0.6,-0.5,0)     )

                NN = Process(target= detect_image, args = (foundObject,))       

                NN.start() 

                #US.start()
                #test.start()
                nav.start()

                
                #test.start()

                NN.join()
                nav.join() 


                
                print("nav has finished")

                

                ########################################################################################
                # Nav 2
                ########################################################################################

                #print("is nav alive? " , nav.is_alive()) 
                print('starting nav2')                
                
                nav2 = Process(target = Navigate, args = (0,0.4,-90,distances,obstacleDetected,foundObject))                  

                nav2.start()

                nav2.join()  

                #    if navIsDone:
                print("nav2 has finished")

                time.sleep(2)

                return

                

                #print("is nav2 alive? " , nav2.is_alive())  

                ########################################################################################
                # Nav 3
                ########################################################################################

                print('starting nav3')
                nav3 =  Process(target = Navigate, args = (0,0.4,-90,distances,obstacleDetected,foundObject))                    

                nav3.start()
                nav3.join()

                #        if navIsDone:
                print("nav3 has finished")

                time.sleep(2)

                

                #print("is nav3 alive? " , nav2.is_alive()) 

                ########################################################################################
                # Nav 4
                ########################################################################################

                print('starting nav4')
                nav4 = Process(target = Navigate, args = (0,0.4,-90,distances,obstacleDetected,foundObject))

                    

                nav4.start()
                nav4.join()

                US.terminate()                

                print("NAV HAS FINISHED")

                output("Finished")


    if scuffed_comp:

        pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000) #Right
        pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000) #Left


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

        print("turning")

        turn(-90)

        
        print("turning finished, going straight")

        direction1.value = forward
        direction2.value = forward

        pwm1.value = 1
        pwm2.value = 1

        print("sleeping for 5 seconds")
        time.sleep(5)

        print("turning left")
        pwm1.value = 0
        pwm2.value = 0

        turn(90)

        print("turn finished, going straight again")


        direction1.value = forward
        direction2.value = forward

        pwm1.value = 1
        pwm2.value = 1

        print("sleeping for 5 seconds")

        time.sleep(5)

        print("turning left")

        pwm1.value = 0
        pwm2.value = 0

        turn(87)

        print("turn finished, going straight for a third time")

        direction1.value = forward
        direction2.value = forward

        pwm1.value = 1
        pwm2.value = 1

        print("sleeping for 5 seconds")

        time.sleep(5)

        print("turning left")

        pwm1.value = 0
        pwm2.value = 0

        turn(87)

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









        

            
        
        # with Manager() as manager:

        #     print("starting navigation...")

        #     distances = manager.list([500,500,500])
        #     obstacleDetected = manager.list([False,False,False])

        #     navIsDone = manager.Value('i',False)

        #     ########################################################################################
        #     # Nav 1
        #     ########################################################################################

        #     US = Process(target = distance, args = (distances,obstacleDetected))

        #     nav = Process(target = Navigate, args = (0,-0.7,-90,distances,obstacleDetected,navIsDone))            

        #     US.start()
        #     #test.start()
        #     nav.start()

            
        #     #test.start()
        #     nav.join() 
            
        #     print("before if ",navIsDone)

        #     #if navIsDone:
        #     print('nav1 has finished')           

        #     time.sleep(2)

        #     navIsDone = False

        #     ########################################################################################
        #     # Nav 2
        #     ########################################################################################

        #     #print("is nav alive? " , nav.is_alive()) 
        #     print('starting nav2')
        #     nav2 = Process(target = Navigate, args = (0,0.7,90,distances,obstacleDetected,navIsDone))                  

        #     nav2.start()

        #     nav2.join()  

        #     #    if navIsDone:
        #     print("nav2 has finished")

        #     time.sleep(2)

        #     navIsDone = False

        #     #print("is nav2 alive? " , nav2.is_alive())  

        #     ########################################################################################
        #     # Nav 3
        #     ########################################################################################

        #     print('starting nav3')
        #     nav3 =  Process(target = Navigate, args = (0,0.7,90,distances,obstacleDetected,navIsDone))                    

        #     nav3.start()
        #     nav3.join()

        #     #        if navIsDone:
        #     print("nav3 has finished")

        #     time.sleep(2)

        #     navIsDone = False

        #     #print("is nav3 alive? " , nav2.is_alive()) 

        #     ########################################################################################
        #     # Nav 4
        #     ########################################################################################

        #     print('starting nav4')
        #     nav4 = Process(target = Navigate, args = (0,0.7,90,distances,obstacleDetected,navIsDone))

                

        #     nav4.start()
        #     nav4.join()

        #     US.terminate()



        #     print("after if ", navIsDone)

        #     print("NAV HAS FINISHED")

            #output("Finished")

main()
f.close()



