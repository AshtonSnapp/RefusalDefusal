#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 7 May 2019
# Changes: Added sequences for easy difficulty
#		   Added way to load a sequence given a difficulty
#		   Added way to run loaded sequence
#####################################################################

# Import necessary modules
import hardware.hardware as hw
import logic.rhClasses as rohe
import graphics.gui as GUI
from random import randint, choice
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

# List of easy mode sequences
# Each sequence has an activity and a hint for that activity
easy_sequences = [{"f100":"Flip switch 1", "p100":"Pull green and blue", "e413":"Enter 413", "f000":"Flip switch 1"}, 
				  {"f010":"Flip switch 2", "p010":"Pull red and and blue", "e2":"Enter 2", "p000":"Pull green", "f000":"Flip switch 2"}, 
				  {"p011":"Pull red", "e24":"Enter 24", "f101":"Flip Switch 1 and 3", "p001":"Pull green"}, 
				  {"p110":"Pull blue", "e41":"Enter 41", "p000":"Pull red and green", "e231":"Enter 231"}]

sequence_loaded = None
sequence = None
#----[MAIN]----------------------------------------------------------
# Start the game
gui.play()

# Main loop...
while(gui.running):
	# Update 
	gui.update()

	# If easy mode selected...
	if(gui.difficulty == "Easy"):

		# Generate an easy sequence if not already generated
		if(sequence_loaded == None):
			sequence_loaded = choice(easy_sequences)
			sequence = sequence_loaded.keys()

	# If user not on a game difficulty, unload sequence
	if(gui.difficulty == "None"):
		sequence_loaded = None

	# Else...
	else:
		# Run first sequence, check if it is completed
		completed = io.run_Sequence(sequence[0])

		# Set the hint text
		gui.hint.set_Text(sequence_loaded[sequence[0]])

		# If completed, go to next activity
    	if(completed):
    		del sequence[0]
    		del sequence_loaded[0]
    		completed = False

	window.update_idletasks()
	window.update()
	sleep(0.01)

# Clean up the hardware
closeGame(io)