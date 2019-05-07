######################################################################
# Name: Justin Crouch
# Date: 23 April 2019
# Description: Counts up on the 7-segment display
######################################################################
import RPi.GPIO as GPIO		# bring in GPIO functionality
from time import sleep

# function that defines the GPIO pins for the nine output LEDs
def setGPIO():
	# define the pins (change these if they are different)
	gpio = [13, 12, 17, 16]
	
	# set them up as output pins
	GPIO.setup(gpio, GPIO.IN, GPIO.PUD_DOWN)

	return gpio


# use the Broadcom pin scheme
GPIO.setmode(GPIO.BCM)

# setup the GPIO pins
gpio = setGPIO()

while(True):
    try:
        for pin in gpio:
            print GPIO.input(pin),

        print

    except KeyboardInterrupt:
        break

GPIO.cleanup()
