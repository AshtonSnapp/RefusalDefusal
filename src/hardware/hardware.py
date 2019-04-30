#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 23 April 2019
# Changes: Hardware Tings
#####################################################################


from RPi.GPIO import * as GPIO


class HardIO(object):
	
	generalPins = [i for i in range(28)]

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		for i in generalPins:
			if i % 2 == 0:
				GPIO.setup(i, GPIO.IN)
			else:
				GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
	def readPin(self, pin):
		if pin % 2 == 0:
			return GPIO.input(pin)
		else:
			raise ValueError("Pin is not a valid input!")

	def setPin(self, pin, value):
		if pin % 2 != 0:
			GPIO.output(pin, value)
		else:
			raise ValueError("Pin is not a valid output!")

	def destroy(self):
		GPIO.cleanup()