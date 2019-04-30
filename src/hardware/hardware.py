#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 23 April 2019
# Changes: Hardware Tings
#####################################################################


from RPi.GPIO import * as GPIO


DEBUG = True


class HardIO(object):
	
	generalPins = [i for i in range(28)]

	def __init__(self):
		GPIO.setmode(GPIO.BCM)

		if (DEBUG):
			print "[H.I/O] Set pin numbering scheme to Broadcom. Hardware Initialization has begun."

		for i in generalPins:
			if i % 2 == 0:
				GPIO.setup(i, GPIO.IN)
				
				if (DEBUG):
					print "[H.I/O] Set pin " + str(i) + " to input."
			else:
				GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
				
				if (DEBUG):
					print "[H.I/O] Set pin " + str(i) + " to output."
	def readPin(self, pin):
		if (pin % 2 == 0) and (pin in generalPins):
			return GPIO.input(pin)
		else:
			if (DEBUG):
				print "[H.I/O] Tried to read pin " + str(pin) + " but it isn't a valid input!"

	def setPin(self, pin, value):
		if (pin % 2 != 0) and (pin in generalPins):
			GPIO.output(pin, value)
		else:
			print "[H.I/O] Tried to set pin " + str(pin) + " but it isn't a valid output!"

	def destroy(self):
		GPIO.cleanup()

		if (DEBUG):
			print "[H.I/O] Cleaned up all the GPIO pins. We're done here boys!"

# List of lists of sequences, which are lists of things to do. First index is difficulty, second index is choice, third index is step.
sequences = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]