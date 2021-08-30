from alignment import align
from obstacle_avoidance import obstacle_avoid
import os
from datetime import datetime
from Pin_Declaration import *
from mapping import *




output("Starting Alignment...")

align()

output("Finished Alignement")

#output("Starting Obstacle Avoidance")

#obstacle_avoid()

#output("Finished Obstacle Avoidance")

output("attempting prelim...")

prelim()

output("finished prelim")


f.close()