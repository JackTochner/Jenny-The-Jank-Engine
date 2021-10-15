from picamera import PiCamera
from time import sleep
import io
import time

camera = PiCamera()

camera.vflip = "True"

camera.hflip = "True"


for i in range(10):
    img_name = "pic" + str(i) + ".jpg"

    camera.capture(img_name)



#camera.capture_continuous("testCont.jpg")

#camera.capture_sequence(["testSeq1.jpg","testSeq2.jpg","testSeq3.jpg","testSeq4.jpg","testSeq5.jpg"])

# camera.record_sequence("testVid.jpg")

# camera.start_record("testVid2.jpg")

# camera.start_preview()
# sleep(5)
# camera.stop_preview()






# stream = io.BytesIO()
# i = 0
# for foo in camera.capture_continuous(stream, format='jpeg'):
#     # Truncate the stream to the current position (in case
#     # prior iterations output a longer image)
#     stream.truncate()
#     stream.seek(0)
#     if  i == 10:
#         break
#     i=i+1

camera.close()