#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 7 May 2019
# Changes: Added functions to handle LED, wires, switches
#		   Added function to run a sequence
#####################################################################
import RPi.GPIO as GPIO
from time import sleep
import os

DEBUG = bool(os.getenv('DEBUG', False))

# Class to handle hardware
class HardIO(object):

	# Pins used
    INPUTS = [5, 4, 22, 23, 24, 25, 26, 27, 12, 6]
    OUTPUTS = [18, 19, 20, 21, 17, 16, 13]

    def __init__(self):
    	# Set up the pinmode to use
        GPIO.setmode(GPIO.BCM)

        if (DEBUG):
            print "[H.I/O] Set pin numbering scheme to Broadcom. Hardware Initialization has begun."

		if (DEBUG):
			print "[H.I/O] Setup input and output pins."

		# Set up input and output pins
        GPIO.setup(HardIO.INPUTS, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(HardIO.OUTPUTS, GPIO.OUT)

        # Instance variables for handling the numpad
        self.numpad_pause = False
        self.set = False
        self.copy = []

    def run_Sequence(self, sequence):
    	completed = False

    	# Check what operation to do
    	# f: check switches, p: check wires, e: check numpad
    	if(sequence[0] == "f"):
    		completed = self.switches(sequence[1:])

    	elif(sequence[0] == "p"):
    		completed = self.switches(sequence[1:])

    	elif(sequence[0] == "e"):
    		# Load the code to use
    		code = [int(c) for c in sequence[1:]]

    		completed = self.numpad(code)

    	return completed

    # Controls RGB LED
    # Value is a string containing 3 integers either 0 or 1
    def RGB(self, value):
    	# What pins to light: R-17 G-16 B-13
    	pinMapping = [17, 16, 13]

    	# Light the LED
    	for i, pin in enumerate(pinMapping):
    		GPIO.output( pin, int(value[i]) )

    # Controls the 7-seg display
    # Value is a string containing two digits: 3, 6, F
    def seven_Seg(self, value):
        # Map string values to pin numbers
        pinMapping = {"3":18, "6":19, "F":20}

		# Turn left side of 7-seg on
		# Turn on path for 3, 6, or F
		GPIO.output( pinMapping[value[0]], 1 )
		GPIO.output( 21, 0 )

        sleep(.01)

		# Turn right side of 7-seg on
		# Turn on path for 3, 6, or F
		GPIO.output( pinMapping[value[0]], 0 )
		GPIO.output( pinMapping[value[1]], 1 )
		GPIO.output( 21, 1 )

        sleep(.01)

        GPIO.output( pinMapping[value[1]], 0 )

    # Reads what wires are plugged in
    # Value is a string containing three digits representing what
    # wires should read high and low; ex: "101" means 1st and
    # 3rd wire should read high while 2nd wire reads low
    # Returns true if value = wire input
    def wires(self, value):
    	# What pins to check
    	pinMapping = [5, 4, 22]

    	# Record wire states
    	_input = "".join( [GPIO.input(pin) for pin in pinMapping] )

    	if(value == _input):
    		return True

    	else:
    		return False

    # Reads what switches are flipped
    # Value is a string containing three digits representing what
    # switches should read high and low; ex: "101" means 1st and
    # 3rd switch should read high while 2nd switch reads low
    # Returns true if value = switch input
    def switches(self, value):
    	# What pins to check
    	pinMapping = [27, 12, 6]

    	# Record wire states
    	_input = "".join( [GPIO.input(pin) for pin in pinMapping] )

    	if(value == _input):
    		return True

    	else:
    		return False

    # Controls and handles numpad
    # code is an array of numbers using 1, 2, 3, or 4
    def numpad(self, code):
        # What pins to check
        pinMapping = [23, 24, 25, 26]

        pressed = []

        if not(self.set):
        	self.copy = [i-1 for i in code]
        	self.set = True
        
        # If more buttons in sequence need to be pressed...
        if(len(self.copy) > 0):

        	# Read state of each pin
            for pin in pinMapping: 
            	pressed.append(GPIO.input(pin))

            # Check if a button is being held down
            if(self.numpad_pause):
                self.numpad_pause = pressed.count(1) > 0

            else:

            	# If one button is pressed...
                if(pressed.count(1) == 1):

                	# Record its index
                    active_index = pressed.index(1)

                    # Check if current button's index is the next button in 
                    # sequence; Remove button if yes
                    if(self.copy[0] == active_index):
                        del self.copy[0]

                    # Reset sequence if no
                    else:
                        self.set = False

                # If a button is pressed, pause numpad handling
                # until button is unpressed
                if(pressed.count(1) > 0):
                    self.numpad_pause = True

            return False

        # If button sequence is empty, return true
        else:
            self.set = False
            return True

    # Cleanup the GPIO pins
    def destroy(self):
        GPIO.cleanup()

        if (DEBUG):
            print "[H.I/O] Cleaned up all the GPIO pins. We're done here boys!"


# List of lists of sequences, which are lists of things to do. First index is difficulty, second index is choice, third index is step.
#sequences = [[['flip(1)', 'pull([2, 3])', 'enter([4, 1, 3])', 'flip(1)'], ['pull(1)', 'enter([2, 4])', 'flip([3, 1])', 'pull(1)'], ['flip(2)', 'pull([1, 3])', 'enter(2)', 'pull([2,3])', 'flip(2)'], ['', '', '', '', '']], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

if(__name__ == "__main__"):
    hIO = HardIO()

    # List containing the sequence to perform
    sequence = ["f101", "p011", "e21324"]
    # List containing what to display on 7-seg
    display_7 = ["36", "6F", "F6"]

    completed = False

    # Loop while there is a sequence
    while(len(sequence) > 0):

    	# Run the current activity
    	# Check if its completed
    	completed = hIO.run_Sequence(sequence[0])

    	# If completed, go to next activity and next 7-seg display
    	if(completed):
    		del sequence[0]
    		del display_7[0]
    		completed = False

        sleep(.01)

    # Flash LED green when the sequence is complete
    for i in range(10):
	    hIO.RGB("010")
	    sleep(.5)

	    hIO.RGB("000")
	    sleep(.5)

	hIO.destroy()