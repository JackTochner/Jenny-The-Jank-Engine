from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.vflip = "True"

camera.hflip = "True"

#camera.capture("testPic.jpg")

#camera.capture_continuous("testCont.jpg")

camera.capture_sequence("[testSeq1.jpg,testSeq2.jpg,testSeq3.jpg,testSeq4.jpg,testSeq5.jpg]")

# camera.record_sequence("testVid.jpg")

# camera.start_record("testVid2.jpg")

camera.start_preview()
sleep(5)
camera.stop_preview()

camera.close()