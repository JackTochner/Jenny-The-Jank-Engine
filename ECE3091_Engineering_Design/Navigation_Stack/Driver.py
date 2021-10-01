import os
from datetime import datetime
from Pin_Declaration import *
from Mapping import *
from Alignment import Align

# need to check if importing only the function will work...

#from Navigation_Main import *
from Navigation import *
from SearchMode import *



def main(align = False, navigate = True, comp=False):

    if align:   
        output("Starting Alignment...")

        Align()

        output("Finished Alignement")

    if navigate:
        output("Starting Navigation")

        Navigate(0,0,-math.pi)

        output("Finished Navigation")

    if comp:
        output("Starting Search...")
        search()
        output("Finished")

f.close()

