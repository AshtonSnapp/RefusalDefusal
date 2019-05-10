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
		  ["f010", "p010", "e2", "f000"], 
		  ["p011", "e24", "f101", "p001"], 
		  ["p110", "e41", "p000", "e231"]]

easy_hints = [["It's lights out for this robot!", "Just line 'em up and knock 'em down!", "I metaphor once. He wanted to be a 3.", "How many people does it take to screw in a light bulb? Two! One to"\
               "screw it in, and another to hold the chair steady... did I say it right?"],
              ["How many people does it take to screw in a light bulb? Two! One to screw it in, and another to hold the chair steady... did I say it right?",\
               "Try pulling her finger. You never know what might happen.", "I'll help you. I just hope I'm not pressing your buttons champ.", "It's lights out for this robot!"],
              ["Just line 'em up and knock 'em down!", "I metaphor once. He wanted to be a 3.", "It's lights out for this robot!", "Try pulling her finger. You never know what might happen."],
              ["Try pulling her finger. You never know what might happen.", "I metaphor once. He wanted to be a 3.", "Just line 'em up and knock 'em down!",\
               "I'll help you. I just hope I'm not pressing your buttons champ."]]

medium_sequences = [["e42", "p100", "f100", "f001", "e31"],
                    ["f101", "p010", "e42143", "p000", "f000"],
                    ["f110", "e12", "p110", "e324", "f011"],
                    ["e34", "p100", "f110", "p000", "e412"]]

medium_hints = [["Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.", "My hair will likely disintegrate if I haven't already pulled it out.",\
                 "I knew I should've switched jobs last week.", "My boss will flip when he hears this!", "According to my calcula- WAIT, where's my calculator?!"],
                ["I knew I should've switched jobs last week.", "My hair will likely disintegrate if I haven't already pulled it out.", "Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.",\
                 "I really hope this doesn't affect the city's power lines.", "I knew I should've switched jobs last week."],
                ["I knew I should've switched jobs last week.", "According to my calcula- WAIT, where's my calculator?!", "My hair will likely disintegrate if I haven't already pulled it out.",\
                 "Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.", "My boss will flip when he hears this!"],
                ["Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.", "I really hope this doesn't affect the city's power lines.",\
                 "I knew I should've switched jobs last week.", "My hair will likely disintegrate if I haven't already pulled it out.", "According to my calcula- WAIT, where's my calculator?!"]]

hard_sequences = 

sequence_hints = []
sequence = []
completed = False
#gameOver = 0 # 0: stop, 1: play, 2: win, 3: lose
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
            sequence_hints = easy_hints[easy_sequences.index(sequence)]

    if(gui.difficulty == "Medium"):

        gui.gameOver = 1

        if(len(sequence) == 0):
            sequence = choice(medium_sequences)
            sequence_hints = medium_hints[medium_sequences.index(sequence)]

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
