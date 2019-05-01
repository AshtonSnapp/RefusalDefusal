#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 23 April 2019
# Changes: Hardware Tings
#####################################################################


import RPi.GPIO as GPIO
from time import sleep


DEBUG = True


class HardIO(object):
	
	Input_pins = sorted([5, 4, 22, 23, 24, 25, 26, 27, 12, 6])
	Output_pins = ([18, 19, 20, 21, 17, 16, 13])

	def __init__(self):
		GPIO.setmode(GPIO.BCM)

		if (DEBUG):
			print "[H.I/O] Set pin numbering scheme to Broadcom. Hardware Initialization has begun."

		'''
		for i in generalPins:
			if i % 2 == 0:
				GPIO.setup(i, GPIO.IN)
				
				if (DEBUG):
					print "[H.I/O] Set pin " + str(i) + " to input."
			else:
				GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
				
				if (DEBUG):
					print "[H.I/O] Set pin " + str(i) + " to output."
		'''

		GPIO.setup(HardIO.Input_pins, GPIO.IN, GPIO.PUD_DOWN)
		GPIO.setup(HardIO.Output_pins, GPIO.OUT)

		GPIO.output(HardIO.Output_pins, 0)

	# Controls the 7-seg display
	# Value is a string containing two digits: 3, 6, F
	def controlSevenSeg(self, value):
		# Map string value to pin numbers
		pinMapping = {"3":18, "6":19, "F":20}

		# Turn left side of 7-seg on
		# Turn on path for specified value
		GPIO.output( pinMapping[value[0]], 1 )
		GPIO.output( 21, 0 )

		sleep(.01)

		# Turn right side of 7-seg on
		# Turn on path for specified value
		GPIO.output( pinMapping[value[0]], 0 )
		GPIO.output( pinMapping[value[1]], 1 )
		GPIO.output( 21, 1 )

		sleep(.01)

		GPIO.output( pinMapping[value[1]], 0 )

	'''
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
	'''

	def destroy(self):
		GPIO.cleanup()

		if (DEBUG):
			print "[H.I/O] Cleaned up all the GPIO pins. We're done here boys!"

# List of lists of sequences, which are lists of things to do. First index is difficulty, second index is choice, third index is step.
sequences = [[['flip(1)', 'pull([2, 3])', 'enter([4, 1, 3])', 'flip(1)'], ['pull(1)', 'enter([2, 4])', 'flip([3, 1])', 'pull(1)'], ['flip(2)', 'pull([1, 3])', 'enter(2)', 'pull([2,3])', 'flip(2)'], ['', '', '', '', '']], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

if(__name__ == "__main__"):
	hIO = HardIO()

	for i in range(2000000):
		hIO.controlSevenSeg("66")
