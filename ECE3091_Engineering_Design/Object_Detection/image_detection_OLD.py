from detecto import core, utils, visualize
from picamera.array import PiRGBArray
from picamera import PiCamera
from processing import *
import cv2
import time
import sys

sys.path.insert(0,"/home/pi/Jenny-The-Jank-Engine/")

#load model
# model = core.Model.load("model_weights_v1.pth", ['Targets'])
model = Model.load("model_weights.pth", ['Targets'])

#Using piCamera grab image fram
# initialize camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)
#grab image from camera
camera.capture(rawCapture, format="bgr")
print("Image Taken!")
image = rawCapture.array

# #Using opencv to grab image frame
# cap = cv2.VideoCapture(0)
# ret, image = cap.read() #ret is a boolean indicating whether the grabbing process was successful or not

# if (ret): 
#     predictions = model.predict(image)

#run image thru model and get predictions
predictions = model.predict(image)
labels, boxes, scores = predictions

# target = scores[0]
print('scores: ',scores)
print("corresponding coords: ", boxes)

# if(target > 0):
#     print('Target Detected!')