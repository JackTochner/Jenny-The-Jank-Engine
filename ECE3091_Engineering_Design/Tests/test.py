from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.capture("testPic.jpg")

# camera.capture_continuous("testCont")

# camera.capture_sequence("testSeq")

# camera.record_sequence("testVid")

# camera.start_record("testVid2")

camera.start_preview()
sleep(5)
camera.stop_preview()

camera.close()