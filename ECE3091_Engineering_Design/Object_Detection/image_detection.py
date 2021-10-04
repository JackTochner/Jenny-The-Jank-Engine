
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

# Load Yolo
model = cv2.dnn.readNet("model_weights_v1.pth", "resnet50.cfg")

# Name custom object
classes = ["Target"]
#reading image
img = cv2.imread("p2.jpg",1) #this can have the image path as well 
blob = cv2.dnn.blobFromImage(img,1/255,(320,320),(0,0,0),swapRB=True,crop=False)

#initialising yolo with image
model.setInput(blob)
output_layers_name = model.getUnconnectedOutLayersNames()
layeroutput = model.forward(output_layers_name)

boxes = []
confidences = []
class_ids = []
width = 320
height = 320

#setting box specifications once object detected
for output in layeroutput:
    for detection in output:
        score = detection[5:]
        class_id = np.argmax(score)
        confidence = score[class_id]
        if confidence > 0.7:
            center_x = int(detection[0]*width)
            center_y = int(detection[0]*height)
            w = int(detection[0]*width)
            h = int(detection[0]*height)
            
            x = int(center_x-w/2)
            y = int(center_y-h/2)
            
            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
            

#len(boxes)
indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0,255,size = (len(boxes),3))

for i in indexes.flatten():
    x,y,w,h = boxes[i]
    
    label = str(class_ids[i])
    confi = str(round(confidences[i],2))
    color = colors[i]
    
    cv2.rectangle(img , (x,y),(x+w,y+h),color,1)
    cv2.putText(img,label+""+confi,(x,y+20),font,2,(255,255,255),1)

#show the resulting image
plt.imshow(img)


