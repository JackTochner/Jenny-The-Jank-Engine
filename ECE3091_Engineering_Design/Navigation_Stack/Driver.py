import os
from datetime import datetime
import sys

sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")
from ECE3091_Engineering_Design.Navigation_Stack.Alignment import *
#from Pin_Declaration import *
#from Mapping import *
#from Alignment import Align

# need to check if importing only the function will work...

#from Navigation_Main import *
from Navigation import *
from SearchMode import *



def main(align = False, navigate = False, comp=True):
   

    if navigate:
        output("Starting Navigation")

        Navigate(0,0,-math.pi)

        output("Finished Navigation")

    if comp:
        output("Starting Search...")     

            
        
        with Manager() as manager:

            distances = manager.list([500,500,500])
            obstacleDetected = manager.list([False,False,False])

            US = Process(target = distance, args = (distances,obstacleDetected))

            nav = Process(target = Navigate, args = (0.5,0,0,distances,obstacleDetected))            

            US.start()
            #test.start()
            nav.start()

            US.join()
            #test.start()
            nav.join() 

            while True:
                if not US.is_alive:
                    print("Ultrasonics are dead")

                if not nav.is_alive:
                    print('nav has finished')

            output("Finished")


f.close()



