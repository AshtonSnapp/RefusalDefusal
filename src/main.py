#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 7 May 2019
# Changes: Added sequences for easy difficulty
#	   Added way to load a sequence given a difficulty
#	   Added way to run loaded sequence
#          Added way to determine if player won or lost
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

#----[SETUP]---------------------------------------------------------
io = hw.HardIO()

# Setup the game
gui, window = GUI.setup()

# List of easy mode sequences
# Each sequence has an activity and a hint for that activity
easy_sequences = [["f100", "p100", "e413", "f000"], 
		  ["f010", "p010", "e2", "p000", "f000"], 
		  ["p011", "e24", "f101", "p001"], 
		  ["p110", "e41", "p000", "e231"]]

easy_hints = [["Flip switch 1", "Pull green and blue", "Enter 413", "Flip switch 1"],
              ["Flip switch 2", "Pull red and and blue", "Enter 2", "Pull green", "Flip switch 2"],
              ["Pull red", "Enter 24", "Flip Switch 1 and 3", "Pull green"],
              ["Pull blue", "Enter 41", "Pull red and green", "Enter 231"]]

sequence_hints = []
sequence = []
completed = 0
#----[MAIN]----------------------------------------------------------
# Start the game
gui.play()

# Main loop...
while(gui.running):
    # Update 
    gui.update()

    # If easy mode selected...
    if(gui.difficulty == "Easy"):

        gui.gameOver = 1
        # Generate an easy sequence if not already generated
        if(len(sequence) == 0):
            sequence = choice(easy_sequences)
            sequence_hints = easy_hints[ easy_sequences.index(sequence) ]

    # If user not on a game difficulty, unload sequence
    if(gui.difficulty == "None"):
        sequence = []

    # Else...
    else:
        if(len(sequence) > 0):
            # Run first sequence, check if it is completed
            completed = io.run_Sequence(sequence[0])

            # Set the hint text
            gui.hint.set_Text(sequence_hints[0])

    # If completed, go to next activity
    if(completed):
        del sequence_hints[0]
        del sequence[0]
        completed = False

    # If completed == 0 (Not Complete), light LED blue
    if(completed == 0):
    	io.RGB("001")

    # If completed == 1 (Failed), light LED red
    if(completed == 1):
    	io.RGB("100")

    # If completed == 2 (Success), light LED green
    if(completed == 1):
    	io.RGB("010")

    if(gui.game_over == 1):
        if(len(sequence) == 0):
            print "You Win!"
            gui.game_over = 2

        elif(gui.timer.end):
            print "You Lose!"
            gui.game_over = 3

    window.update_idletasks()
    window.update()
    sleep(0.01)

# Clean up the hardware
closeGame(io)
