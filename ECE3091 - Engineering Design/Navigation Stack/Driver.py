from alignment import align
from obstacle_avoidance import obstacle_avoid
import os
from datetime import datetime
from Pin_Declaration import *




print("Starting Alignment...")
f.write("Starting Alignement...\n")

align()

print("Finished Alignement")
f.write("Finished Alignement\n")

#print("Starting Obstacle Avoidance")
#f.write("Starting Obstacle Avoidance\n")

#obstacle_avoid()

#print("Finished Obstacle Avoidance")
#f.write("Finished Obstacle Avoidance\n")

f.close()