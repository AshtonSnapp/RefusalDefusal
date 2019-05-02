#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 23 April 2019
# Changes: Hardware Tings
#####################################################################
import RPi.GPIO as GPIO
from time import sleep


DEBUG = True


class HardIO(object):
    Input_pins = [5, 4, 22, 23, 24, 25, 26, 27, 12, 6]
    Output_pins = [18, 19, 20, 21, 17, 16, 13]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        if (DEBUG):
            print "[H.I/O] Set pin numbering scheme to Broadcom. Hardware Initialization has begun."

        GPIO.setup(HardIO.Input_pins, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(HardIO.Output_pins, GPIO.OUT)

        self.numpad_pause = False
        self.code = []
        self.copy = []

    # Controls the 7-seg display
    # Value is a string containing two digits: 3, 6, F
    def controlSevenSeg(self, value):
        # Map string values to pin numbers
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

    # Controls and handles numpad
    # code is an array of numbers: 0, 1, 2, 3
    def controlNumpad(self):
        # Map string values to pin numbers
        pinMapping = [23, 24, 25, 26]

        pressed = []
        
        if(len(self.copy) > 0):
            for pin in pinMapping: pressed.append(GPIO.input(pin))

            if(self.numpad_pause):
                self.numpad_pause = pressed.count(1) > 0

            else:
                if(pressed.count(1) == 1):
                    active_index = pressed.index(1)

                    if(self.copy[0] == active_index):
                        del self.copy[0]

                    else:
                        self.copy = [i for i in self.code]

                if(pressed.count(1) > 0):
                    self.numpad_pause = True

        else:
            print "Open"
            return True

    def setCode(self, code):
        self.code = [i for i in code]
        self.copy = [i for i in code]

    def destroy(self):
        GPIO.cleanup()

        if (DEBUG):
            print "[H.I/O] Cleaned up all the GPIO pins. We're done here boys!"


# List of lists of sequences, which are lists of things to do. First index is difficulty, second index is choice, third index is step.
sequences = [[['flip(1)', 'pull([2, 3])', 'enter([4, 1, 3])', 'flip(1)'], ['pull(1)', 'enter([2, 4])', 'flip([3, 1])', 'pull(1)'], ['flip(2)', 'pull([1, 3])', 'enter(2)', 'pull([2,3])', 'flip(2)'], ['', '', '', '', '']], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

if(__name__ == "__main__"):
    hIO = HardIO()

    hIO.setCode([0, 2, 1, 3])

    for i in range(10000):
        hIO.controlSevenSeg("36")
            
        hIO.controlNumpad()
