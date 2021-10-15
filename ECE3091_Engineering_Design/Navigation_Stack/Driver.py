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

            US = Process(target = distance, args = (distances,obstacleDetected))

            nav = Process(target = Navigate, args = (0,-0.7,-90,distances,obstacleDetected,navIsDone))            

            US.start()
            #test.start()
            nav.start()

            
            #test.start()
            nav.join() 
            
            print("before if ",navIsDone)

            if navIsDone:
                print('nav1 has finished')

                time.sleep(2)

                navIsDone = 0

                nav2 = Process(target = Navigate, args = (0.7,0,90,distances,obstacleDetected,navIsDone))   

                nav2.start()

                nav2.join()  

                if navIsDone:
                    print("nav2 has finished")

                    time.sleep(2)

                    navIsDone = 0

                    nav3 =  Process(target = Navigate, args = (0,0.7,90,distances,obstacleDetected,navIsDone)) 

                    nav3.start()
                    nav3.join()

                    if navIsDone:
                        print("nav3 has finished")

                        nav4 = Process(target = Navigate, args = (-0.7,0.0,90,distances,obstacleDetected,navIsDone))

                        nav4.start()
                        nav4.join()

                        US.terminate()



            print("after if ", navIsDone)

            #output("Finished")

main()
f.close()



