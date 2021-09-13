import RPi.GPIO as GPIO

electromagnet_pin = 20

GPIO.setmode(GPIO.BOARD)
GPIO.setup(electromagnet_pin, GPIO.OUT)


def electromagnet(self, on):
	output = GPIO.HIGH if on else GPIO.LOW
	GPIO.output(electromagnet_pin, output)
	


# Dynamically turn on/off electromagnet - test for on and off
while true
	electromagnet(True) # On

	sleep(10)

	electromagnet(False) # Off

# pseudo for performing actions
# resting state of the gripper is parallel to the floor
# once it has stopped in front of a steel ball bearing, 
	# rotate the gripper towards the floor 'x' degrees 
	# turn on the electromagnet
	# rotate it all the way back 'y' degrees (over 180) to stop above the bucket
	# turn off the electromagnet
	# wait like 2 seconds
	# return to resting state
	# wait for next target to be reached

# def grabTarget():
# 	setAngle(30)