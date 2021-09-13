import os
from datetime import datetime
from Pin_Declaration import *
from Mapping import *
from Alignment import Align

# need to check if importing only the function will work...

#from Navigation_Main import *
from Navigation_Main import Navigate



def main(align = False, navigate = True):

    if align:   
        output("Starting Alignment...")

        Align()

        output("Finished Alignement")

    if navigate:
        output("Starting Navigation")

        Navigate()

        output("Finished Navigation")

f.close()

