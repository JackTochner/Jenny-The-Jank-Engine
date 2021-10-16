import os
from datetime import datetime
import sys

sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")
#from ECE3091_Engineering_Design.Navigation_Stack.Alignment import *
#from Pin_Declaration import *
#from Mapping import *
#from Alignment import Align

# need to check if importing only the function will work...

#from Navigation_Main import *
from Navigation import *
#from SearchMode import *



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

                navIsDone = manager.Value('i',False)

                ########################################################################################
                # Nav 1
                ########################################################################################

                US = Process(target = distance, args = (distances,obstacleDetected))

                nav = Process(target = Navigate, args = (0,-0.7,-90,distances,obstacleDetected,navIsDone))            

                US.start()
                #test.start()
                nav.start()

                
                #test.start()
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



