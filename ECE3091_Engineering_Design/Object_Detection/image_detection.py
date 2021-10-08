from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image, plot_prediction_grid
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time

#load model
model = core.Model.load('model_weights_v1.pth', ['Targets'])

#Using piCamera grab image fram
#initialize camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)
#grab image from camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#Using opencv to grab image frame
# cap = cv2.VideoCapture(0)
# ret, image = cap.read() #ret is a boolean indicating whether the grabbing process was successful or not

# if ret: 
#     predictions = model.predict(image)


#run image thru model and get predictions
predictions = model.predict(image)
labels, boxes, scores = predictions

target = scores[0]
print('top score: ',target)
print("corresponding coords: ", boxes[0])

if(target > 0):
    print('Target Detected!')