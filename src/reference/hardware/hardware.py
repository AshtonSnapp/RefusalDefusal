#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 7 May 2019
# Changes: Added functions to handle LED, wires, switches
#		   Added function to run a sequence
#####################################################################
import RPi.GPIO as GPIO
from time import sleep, time
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

        for pin in HardIO.OUTPUTS:
            GPIO.output(pin, 0)

        self.codeIn = ""
        self.held = False
        self.code_index = 1

        self.wire_wait = 0
        
        self.seven_seg_counter = 0
        self.seven_seg_index = -1

        self.prev_wires = "111"
        self.prev_switches = "000"
        self.prev_code = ""

        self.mistakes = 0

    def reset(self):
        self.codeIn = ""
        self.held = False
        self.code_index = 1

        self.wire_wait = 0
        
        self.seven_seg_counter = 0
        self.seven_seg_index = -1

        self.prev_wires = "111"
        self.prev_switches = "000"
        self.prev_code = ""

        self.mistakes = 0

    def run_Sequence(self, sequence):
        completed = False
        
        wires = self.wires()
        switches = self.switches()
        self.numpad()

        # If the activity is to flip...
        if(sequence[0] == "f"):

            self.display_7_Seg(sequence, switches)
            
            # Check if the other inputs have changed; if so, add to mistakes
            if(wires != self.prev_wires or self.codeIn != self.prev_code):
                self.mistakes += 1

            # If switch status has changed and equals the sequence, return true for completed
            elif(switches != self.prev_switches and switches == sequence[1:]):
                completed = True

            # If switch status has changed and not equals the sequence...
            elif(switches != self.prev_switches and switches != sequence[1:]):
                
                # Add to mistakes however many wrong switches flipped...
                for i in range(3):
                    if(switches[i] != self.prev_switches[i] and switches[i] != sequence[i+1]):
                        self.mistakes += 1

            # Reset code
            self.codeIn = ""

        # If the activity is to pull...
        elif(sequence[0] == "p"):

            self.display_RGB(sequence[1:])
            
            # Check if the other inputs have changed; if so, add to mistakes
            if(switches != self.prev_switches or self.codeIn != self.prev_code):
                self.mistakes += 1

            # If wire status has changed and equals the sequence, return true for completed
            elif(wires != self.prev_wires and wires == sequence[1:]):
                completed = True

            # If wire status has changed and not equals the sequence...
            elif(wires != self.prev_wires and wires != sequence[1:]):
                
                # Add to mistakes however many wrong wires pulled...
                for i in range(3):
                    if(wires[i] != self.prev_wires[i] and wires[i] != sequence[i+1]):
                        self.mistakes += 1

            # Reset code
            self.codeIn = ""

        # If the activity is to enter...
        elif(sequence[0] == "e"):

            self.display_7_Seg(sequence)
            
            # Check if the other inputs have changed; if so, add to mistakes
            if(switches != self.prev_switches or wires != self.prev_wires):
                self.mistakes += 1

            # If code status has changed and equals the sequence, return true for completed
            elif(self.codeIn != self.prev_code and self.codeIn == sequence[1:]):
                completed = True
                self.codeIn = ""

             # If code status has changed and equals the sequence, return true for completed
            elif(self.codeIn != self.prev_code and self.codeIn != sequence[1:self.code_index]):
                self.mistakes += 1
                self.codeIn = ""
                self.code_index = 1

        if(sequence[0] != "e"):
            self.codeIn = ""
            self.prev_code = ""

        self.prev_wires = wires
        self.prev_switches = switches
        self.prev_code = self.codeIn
        
        return completed

    def display_RGB(self, sequence):
        light = ""

        for s in sequence:
            if(s == "1"): light += "0"
            else: light += "1"

        self.RGB(light)

    def display_7_Seg(self, value, _input=None):
        sequence = value[1:]
        timing = time()

        if(value[0] == "f"):
            if( abs(time()-self.seven_seg_counter) > .5):
                self.seven_seg_counter = time()
                self.seven_seg_index += 1
                
            if(self.seven_seg_index >= 3):
                self.seven_seg_index = 0

            if(sequence[self.seven_seg_index] != _input[self.seven_seg_index]):
                self.seven_Seg("0" + str(self.seven_seg_index+1))

        elif(value[0] == "e"):
            if( timing-self.seven_seg_counter > .75):
                self.seven_seg_index += 1

                if(self.seven_seg_index == len(sequence)-1):
                    self.seven_seg_counter = time() + .5

                else:
                    self.seven_seg_counter = time()

            if(self.seven_seg_index >= len(sequence)):
                    self.seven_seg_index = 0

            if( timing-self.seven_seg_counter < .5 ):
                if(sequence[self.seven_seg_index] != "4"):
                    self.seven_Seg("0" + sequence[self.seven_seg_index])

                else:
                    self.seven_Seg("02")
                    self.seven_Seg("12")
                
    # Controls RGB LED
    # Value is a string containing 3 integers either 0 or 1
    def RGB(self, value):
    	# What pins to light: R-25 G-26 B-27
    	pinMapping = [25, 26, 27]

    	# Light the LED
    	for i, pin in enumerate(pinMapping):
    	    GPIO.output( pin, int(value[i]) )

    # Controls the 7-seg display
    # Value is a string containing two digits: 0, 1, 2, 3
    def seven_Seg(self, value):
        # Map string values to pin numbers
        pinMapping = {"1":6, "2":5, "3":4}

        # Turn a side of 7-seg on
        # Turn on path for 1, 2, 3
        if(value[1] != "0"):
            GPIO.output( pinMapping[value[1]], 1 )
            GPIO.output( 12, int(value[0]) )

            sleep(.01)
            
            GPIO.output( pinMapping[value[1]], 0 )

    # Reads what wires are plugged in
    # Value is a string containing three digits representing what
    # wires should read high and low; ex: "101" means 1st and
    # 3rd wire should read high while 2nd wire reads low
    # Returns 2 if value = wire input, 1 if value != wire input
    # 0 if the state has not changed
    def wires(self):
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

        if( abs(time()-self.wire_wait) > 0.5 and _input != self.prev_wires):
            self.wire_wait = time()

            return _input

        else:
            return self.prev_wires

    # Reads what switches are flipped
    # Value is a string containing three digits representing what
    # switches should read high and low; ex: "101" means 1st and
    # 3rd switch should read high while 2nd switch reads low
    # Returns true if value = switch input
    def switches(self):
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

        return _input

    # Controls and handles numpad
    # code is an array of numbers using 1, 2, 3, or 4
    def numpad(self):
        # What pins to check
        pinMapping = [23, 24, 21, 22]

        pressed = [GPIO.input(pin) for pin in pinMapping]
        any_pressed = False

        for i in pressed:
            if(i): any_pressed = True

        if(any_pressed and not self.held):
            self.held = True
            self.code_index += 1
                        
            if(pressed[0]): self.codeIn += "1"
            if(pressed[1]): self.codeIn += "2"
            if(pressed[2]): self.codeIn += "3"
            if(pressed[3]): self.codeIn += "4"

        elif(not any_pressed and self.held):
            self.held = False

    # Cleanup the GPIO pins
    def destroy(self):
        GPIO.cleanup()

        if (DEBUG):
            print "[H.I/O] Cleaned up all the GPIO pins. We're done here boys!"


if(__name__ == "__main__"):
    hIO = HardIO()

    completed = False
    
    while(True):

        if(not completed):
            completed = hIO.run_Sequence("e1234321")

        else:
            break


    
    hIO.destroy()
