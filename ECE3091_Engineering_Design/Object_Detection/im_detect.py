
import cv2
import numpy as np
import glob
import random
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

# Load Yolo
net = cv2.dnn.readNet("yolov4best.weights", "yolov4-tiny-detector.cfg")
# Name custom object
labels = ["Targets"]
i = 0
k = 0 
while k < 1:
    camera = PiCamera()
    i += 1
    k += 1
    camera.vflip = "True"

    camera.hflip = "True"
    image_name = "pic" + str(i) + ".jpg"
    camera.capture(image_name)

    #reading image running thru network
    image = cv2.imread(image_name,1)
    h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image,1/255.0,(416,416),(0,0,0),swapRB=True,crop=False)

    # sets the blob as the input of the network
    net.setInput(blob)
    # get all the layer names
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    # feed forward (inference) and get the network output
    # measure how much it took in seconds
    start = time.perf_counter()
    layer_outputs = net.forward(ln)
    time_took = time.perf_counter() - start
    print(f"Time took: {time_took:.2f}s")

    #looping through images and getting coordinates
    font_scale = 2
    thickness = 5
    boxes, confidences, class_ids = [], [], []
    # loop over each of the layer outputs
    for output in layer_outputs:
        # loop over each of the object detections
        for detection in output:
            # extract the class id (label) and confidence (as a probability) of
            # the current object detection
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # discard out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > 0.1:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = box.astype("int")
                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    if len(confidences) > 0:
        top_score = max(confidences);   
        top_ind = confidences.index(top_score)
        #boxes to be done
        x_coord = boxes[top_ind][0]
        y_coord = boxes[top_ind][1]
        width = boxes[top_ind][2]
        height = boxes[top_ind][3]

        print('top_score:',top_score)
        print('x: ', x_coord)
        print('y: ', y_coord)   
        print('w: ', width)
        print('h: ', height)  
    else:
        print("Confidences is empty!")
