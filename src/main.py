#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 1 May 2019
# Changes: Adjusted way of importing hardware, logic, and gui classes
#		   Added manual mainloop
#		   Adjusted way of displaying the gui
#####################################################################

# Import necessary modules
import hardware.hardware as hw
import logic.rhClasses as rohe
import graphics.gui as GUI
from random import randint
from time import sleep

#----[FUNCTIONS]-----------------------------------------------------
# A function to be called that safely closes everything down. Takes in a reference to a HardIO object.
def closeGame(hard_io):
	# Closing remarks to be printed when the game closes. Feel free to add your own strings!
	closingRemarks = ["Have an awesome day!", "May the force be with you.", "Thank you for playing!", "Exited with status code 0 - success!", "b a n a n a"]

	hard_io.destroy()

	print closingRemarks[randint(0, len(closingRemarks) - 1)]

	exit(0)

#----[SETUP]---------------------------------------------------------
io = hw.HardIO()

# Setup the game
gui, window = GUI.setup()

#----[MAIN]----------------------------------------------------------
# Start the game
gui.play()

# Main loop...
while(gui.running):

	# Update 
	gui.update()
	window.update_idletasks()
	window.update()
	sleep(0.01)

# Clean up the hardware
closeGame(io)

'''
execfile("./graphics/gui.py")

if not (gui.running):
	closeGame(io)
'''