######################################################################
# Name: Justin Crouch
# Date: 23 April 2019
# Description: Counts up on the 7-segment display
######################################################################
import RPi.GPIO as GPIO		# bring in GPIO functionality
from random import randint	# to generate random integers
from time import sleep

# function that defines the GPIO pins for the nine output LEDs
def setGPIO():
	# define the pins (change these if they are different)
	gpio = [i for i in range(23, 28)]
	
	# set them up as output pins
	GPIO.setup(gpio, GPIO.OUT)

	return gpio


# use the Broadcom pin scheme
GPIO.setmode(GPIO.BCM)

# setup the GPIO pins
gpio = setGPIO()

# Set all pins to LOW
for pin in gpio:
    GPIO.output(pin, 0)

# Variables to track what number to display
counter = 1
right_index = 1
left_index = 1

while(True):
    try:
        # Turn on LED for the right side
        # Turn off LED for the left side
        # Set the side selector to HIGH (right side)
        GPIO.output(gpio[left_index], 0)
        GPIO.output(gpio[right_index], 1)
        
        GPIO.output(gpio[0], 1)

        sleep(.005)

        # Turn on LED for the left side
        # Turn off LED for the right side
        # Set the side selector to LOW (left side)
        GPIO.output(gpio[right_index], 0)
        GPIO.output(gpio[left_index], 1)
        GPIO.output(gpio[0], 0)

        sleep(.005)

        # Countinue to count up
        counter += .2
        if(counter > 10):
            counter = 1

            GPIO.output(gpio[right_index], 0)

            right_index += 1
            if(right_index > 4):
                right_index = 1

                GPIO.output(gpio[left_index], 0)

                left_index += 1
                if(left_index > 4):
                    left_index = 1

    except KeyboardInterrupt:
        break

# clean up and reset the GPIO pins
for pin in gpio:
    GPIO.output(pin, 0)

GPIO.cleanup()

