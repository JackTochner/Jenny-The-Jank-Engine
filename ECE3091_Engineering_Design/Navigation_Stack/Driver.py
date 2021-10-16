import os
from datetime import datetime
import sys
#from ECE3091_Engineering_Design.Object_Detection import im_detect

sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")
#from ECE3091_Engineering_Design.Navigation_Stack.Alignment import *
#from Pin_Declaration import *
#from Mapping import *
#from Alignment import Align

# need to check if importing only the function will work...

#from Navigation_Main import *
from Navigation import *
from im_detect import *
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


def main(align = False, navigate = False, comp=True):
   

    if navigate:
        #output("Starting Navigation")

        Navigate(0,0,-math.pi)

        #output("Finished Navigation")

    if comp:
        #output("Starting Search...")     


            with Manager() as manager:

                print("starting navigation...")

                distances = manager.list([500,500,500])
                obstacleDetected = manager.list([False,False,False])

                check = manager.Value('i',0)

                ########################################################################################
                # Nav 1
                ########################################################################################

                print("turning...")

                #turn(-90)
                print("not actually turning lol")

                print("finished turning")

                time.sleep(2)

                US = Process(target = distance, args = (distances,obstacleDetected))

                nav = Process(target = Navigate, args = (0.1,0,0,distances,obstacleDetected))    

                NN = Process(target= detect_image)       

                NN.start() 

                US.start()
                #test.start()
                nav.start()

                
                #test.start()

                NN.join()
                nav.join() 
                
                print("nav has finished")





        

            
        
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



