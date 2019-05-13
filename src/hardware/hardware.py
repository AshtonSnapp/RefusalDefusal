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
    INPUTS = [17, 16, 13, 18, 19, 20, 21, 22, 23, 24]
    OUTPUTS = [12, 6, 5, 4, 25, 26, 27]

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

        # Variables to check if a state has changed
        self.state_changed = False
        self.last_state = None

    def run_Sequence(self, sequence):
    	completed = False

    	# Check what operation to do
    	# f: check switches, p: check wires, e: check numpad
    	if(sequence[0] == "f"):
            self.last_state = sequence[1:]
    	    completed = self.switches(sequence[1:])

    	elif(sequence[0] == "p"):
            self.last_state = sequence[1:]
    	    completed = self.wires(sequence[1:])

    	elif(sequence[0] == "e"):
    	    # Load the code to use
    	    code = [int(c) for c in sequence[1:]]

    	    completed = self.numpad(code)

    	return completed

    # Controls RGB LED
    # Value is a string containing 3 integers either 0 or 1
    def RGB(self, value):
    	# What pins to light: R-17 G-16 B-13
    	pinMapping = [25, 26, 27]

    	# Light the LED
    	for i, pin in enumerate(pinMapping):
    	    GPIO.output( pin, int(value[i]) )

    # Controls the 7-seg display
    # Value is a string containing two digits: 3, 6, F
    def seven_Seg(self, value):
        # Map string values to pin numbers
        pinMapping = {"3":12, "6":6, "F":5}

        # Turn left side of 7-seg on
        # Turn on path for 3, 6, or F
        GPIO.output( pinMapping[value[0]], 1 )
        GPIO.output( 4, 0 )

        sleep(.01)

        # Turn right side of 7-seg on
        # Turn on path for 3, 6, or F
        GPIO.output( pinMapping[value[0]], 0 )
        GPIO.output( pinMapping[value[1]], 1 )
        GPIO.output( 4, 1 )

        sleep(.01)

        GPIO.output( pinMapping[value[1]], 0 )

    # Reads what wires are plugged in
    # Value is a string containing three digits representing what
    # wires should read high and low; ex: "101" means 1st and
    # 3rd wire should read high while 2nd wire reads low
    # Returns 2 if value = wire input, 1 if value != wire input
    # 0 if the state has not changed
    def wires(self, value):
        # What pins to check
        pinMapping = [20, 19, 18]

        # Record wire states
        _input = [GPIO.input(pin) for pin in pinMapping]

        for i in range(len(_input)):
            if(_input[i] == True):
                _input[i] = "1"

            else:
                _input[i] = "0"

        _input = "".join(_input)

        # Check if state has changed
        if(_input != self.last_state):
            self.state_changed = True
        else:
            self.state_changed = False

        self.last_state = _input

        # If state is different, check if it is the correct state
        if(self.state_changed):
            if(value == _input):
                return 2

            elif(value != _input):
                return 1

        else:
            return 0

    # Reads what switches are flipped
    # Value is a string containing three digits representing what
    # switches should read high and low; ex: "101" means 1st and
    # 3rd switch should read high while 2nd switch reads low
    # Returns true if value = switch input
    def switches(self, value):
        # What pins to check
        pinMapping = [17, 16, 13]

        # Record wire states
        _input = [not GPIO.input(pin) for pin in pinMapping]
    	
        for i in range(len(_input)):
            if(_input[i] == True):
                _input[i] = "1"

            else:
                _input[i] = "0"

        _input = "".join(_input)

        if(value == _input):
            return True

        else:
            return False

    # Controls and handles numpad
    # code is an array of numbers using 1, 2, 3, or 4
    def numpad(self, code):
        # What pins to check
        pinMapping = [23, 24, 21, 22]

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


if(__name__ == "__main__"):
    hIO = HardIO()

    # List containing the sequence to perform
    sequence = ["f101", "e21324", "p011"]
    # List containing what to display on 7-seg
    display_7 = ["36", "6F", "F6"]

    completed = False

    print sequence[0]

    # Loop while there is a sequence
    while(len(sequence) > 0):

        # Run the current activity
        # Check if its completed
        completed = hIO.run_Sequence(sequence[0])

        # If completed, go to next activity and next 7-seg display
        if(completed):
            del sequence[0]
            del display_7[0]

            if(len(sequence) > 0):
                print sequence[0]

            completed = False

        sleep(.01)

    # Flash LED green when the sequence is complete
    for i in range(10):
        hIO.RGB("010")
        sleep(.5)

        hIO.RGB("000")
        sleep(.5)

    hIO.destroy()
