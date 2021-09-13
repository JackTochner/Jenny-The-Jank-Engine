import RPi.GPIO as GPIO

electromagnet_pin = 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(electromagnet_pin, GPIO.OUT)


def electromagnet(self, on):
	output = GPIO.HIGH if on else GPIO.LOW
	GPIO.output(electromagnet_pin, output)
	


# Dynamically turn on/off electromagnet
while true
	electromagnet(True) # On

	sleep(10)

	electromagnet(False) # Off

#pseudo