from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image, plot_prediction_grid
from picamera.array import PiRGBArray
from picamera import PiCamera

#load model
model = core.Model.load('model_weights_v1.pth', ['Targets'])
#initialize camera
camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

#grab image from camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
#image = utils.read_image(im) #
#run image thru model and get predictions
predictions = model.predict(image)
labels, boxes, scores = predictions

target = scores[0]
print('top score: ',target)
print("corresponding coords: ", boxes[0])

if(target > 0):
    print('Target Detected!')