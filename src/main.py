#####################################################################
# Original Authors: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 2 FEB 2024
# Description:
#   Desktop version of our Raspberry Pi project.
#   Updated to Python 3
#####################################################################

# Import necessary modules
# import hardware.hardware as hw
import graphics.gui as GUI
# import Sequences.Sequence_Generator as Seq_Gen
from random import randint, choice
from time import sleep

#----[FUNCTIONS]-----------------------------------------------------
# A function to be called that safely closes everything down. Takes in a reference to a HardIO object.
def closeGame(hard_io):
	# Closing remarks to be printed when the game closes. Feel free to add your own strings!
	closingRemarks = ["Have an awesome day!", "May the force be with you.", "Thank you for playing!", "Exited with status code 0 - success!", "b a n a n a"]

	# hard_io.destroy()

	print(choice(closingRemarks))

#----[SETUP]---------------------------------------------------------
# io = hw.HardIO()
# gen = Seq_Gen.SequenceGenerator()

# Setup the game
gui, window = GUI.setup()

# List of easy mode sequences
# Each sequence has an activity and a hint for that activity
sequences = [["f100", "p100", "e43", "f000"], 
		  ["f010", "p010", "e23", "f000"], 
		  ["p011", "e42", "f101", "p001"], 
		  ["p110", "e41", "p000", "e23"]]

hints = [["It's lights out for this robot!", "Just line 'em up and knock 'em down!", "I metaphor once. He wanted to be a 3.", "How many people does it take to screw in a light bulb? Two! One to screw it in, and another to hold the chair steady... did I say it right?"],
              ["How many people does it take to screw in a light bulb? Two! One to screw it in, and another to hold the chair steady... did I say it right?",\
               "Try pulling her finger. You never know what might happen.", "I'll help you. I just hope I'm not pressing your buttons champ.", "It's lights out for this robot!"],
              ["Just line 'em up and knock 'em down!", "I metaphor once. He wanted to be a 2.", "It's lights out for this robot!", "Try pulling her finger. You never know what might happen."],
              ["Try pulling her finger. You never know what might happen.", "I metaphor once. He wanted to be a 3.", "Just line 'em up and knock 'em down!",\
               "I'll help you. I just hope I'm not pressing your buttons champ."]]

# for i, sequence in enumerate(sequences):
# 	gen.addSeq("Easy", sequence, hints[i])


# List of medium mode sequences
# Each sequence has an activity and a hint for that activity
sequences = [["e42", "p100", "f100", "f001", "e31"],
                    ["f101", "p010", "e2143", "p000", "f000"],
                    ["f110", "e12", "p110", "e3243", "f011"],
                    ["e34", "p100", "f110", "p000", "e4112"]]

hints = [["Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.", "My hair will likely disintegrate if I haven't already pulled it out.",\
                 "I knew I should've switched jobs last week.", "My boss will flip when he hears this!", "According to my calcula- WAIT, where's my calculator?!"],
                ["I knew I should've switched jobs last week.", "My hair will likely disintegrate if I haven't already pulled it out.", "Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.",\
                 "I really hope this doesn't affect the city's power lines.", "I knew I should've switched jobs last week."],
                ["I knew I should've switched jobs last week.", "According to my calcula- WAIT, where's my calculator?!", "My hair will likely disintegrate if I haven't already pulled it out.",\
                 "Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.", "My boss will flip when he hears this!"],
                ["Don't fret over a lawsuit. You can leave those pressing matters to me. Having said that, please don't fail.", "I really hope this doesn't affect the city's power lines.",\
                 "I knew I should've switched jobs last week.", "My hair will likely disintegrate if I haven't already pulled it out.", "According to my calcula- WAIT, where's my calculator?!"]]

# for i, sequence in enumerate(sequences):
# 	gen.addSeq("Medium", sequence, hints[i])


# List of hard mode sequences
# Each sequence has an activity and a hint for that activity
sequences = [["f110", "p101", "e1424", "f100", "p100"],
                  ["p110", "f010", "f000", "e4431", "p010", "e2233"],
                  ["f111", "p010", "e4131", "f001", "e22"],
                  ["e4121", "p001", "f001", "e2114", "f010", "p000"]]

hints = [["If you survive this, feel free to come over and play on my switch.", "Firmly grasp it bro!", "...Have you tried pressing the reset button?", \
               "I'm having a hard time seeing the problem here. Got a light?", "Why're you building a robot anyway when you could be relaxing?"],
              ["Why're you building a robot anyway when you could be relaxing?", "If you survive this, feel free to come over and play on my switch.", "If you survive this, feel free to come over and play on my switch.", \
               "...Have you tried pressing the reset button?", "Firmly grasp it bro!", "To succeed here, you must enter a new state of being. That's what a fortune cookie told me at least."],
              ["I'm having a hard time seeing the problem here. Got a light?", "Why're you building a robot anyway when you could be relaxing?", \
              "To succeed here, you must enter a new state of being. That's what a fortune cookie told me at least.", "If you survive this, feel free to come over and play on my switch."\
              "...Have you tried pressing the reset button?"],
              ["...Have you tried pressing the reset button?", "Firmly grasp it bro!", "If you survive this, feel free to come over and play on my switch.", \
               "To succeed here, you must enter a new state of being. That's what a fortune cookie told me at least.", "I'm having a hard time seeing the problem here. Got a light?", \
               "Why're you building a robot anyway when you could be relaxing?"]]

# for i, sequence in enumerate(sequences):
# 	gen.addSeq("Hard", sequence, hints[i])


# List of real life mode sequences
# Each sequence has an activity and a hint for that activity
sequences = [["f101", "p011", "e1424", "f100", "p010"],
                      ["p110", "f010", "f000", "e1344", "p010", "e2331"],
                      ["f111", "p010", "e4131", "f001", "e22"],
                      ["e4121", "p001", "f001", "e2234", "f010", "p000"]]

hints = [["If you're not successful I'll have to switch your sleeping bag with a body bag.", "You'd better find your head and pull it out before I do it for you!", \
                   "A good soldier always presses on.", "I've seen someone defuse a bomb while flipping and sprinting. What's your excuse?", \
                   "Pull up your britches and get to defusing maggot!"],
                  ["You'd better find your head and pull it out before I do it for you!", "I've seen someone defuse a bomb while flipping and sprinting. What's your excuse?", \
                   "If you're not successful I'll have to switch your sleeping bag with a body bag.", "Drop and give me 20!", \
                   "You'd better find your head and pull it out before I do it for you!", "A good soldier always presses on."],
                  ["I've seen someone defuse a bomb while flipping and sprinting. What's your excuse?", "You'd better find your head and pull it out before I do it for you!", \
                  "A good soldier always presses on.", "If you're not successful I'll have to switch your sleeping bag with a body bag.", "Drop and give me 20!"],
                  ["A good soldier always presses on.", "Pull up your britches and get to defusing maggot!", "If you're not successful I'll have to switch your sleeping bag with a body bag.", \
                   "Drop and give me 20!", "I've seen someone defuse a bomb while flipping and sprinting. What's your excuse?", "Pull up your britches and get to defusing maggot!"]]

# for i, sequence in enumerate(sequences):
# 	gen.addSeq("RealLife", sequence, hints[i])


completed = False
#----[MAIN]----------------------------------------------------------
# Start the game
gui.play()

# # Main loop...
# while(gui.running):
#     # Update 
#     gui.update()

#     # If easy mode selected...
#     if(gui.difficulty == "Easy"):

#         gui.gameOver = 1
        
#         # Generate an easy sequence if not already generated
#         if(gen.getSeqLen() == 0):
#             gen.genSequence("Easy")
#             io.reset()


#     # If medium mode selected...
#     elif(gui.difficulty == "Medium"):

#         gui.gameOver = 1
        
#         # Generate a medium sequence if not already generated
#         if(gen.getSeqLen() == 0):
#             gen.genSequence("Medium")
#             io.reset()
#             gui.mistake.max = 10


#     # If hard mode selected...
#     elif(gui.difficulty == "Hard"):

#         gui.gameOver = 1
        
#         # Generate a hard sequence if not already generated
#         if(gen.getSeqLen() == 0):
#             gen.genSequence("Hard")
#             io.reset()
#             gui.mistake.max = 5


#     # If real life mode selected...
#     elif(gui.difficulty == "Real Life"):

#         gui.gameOver = 1
        
#         # Generate a RealLife sequence if not already generated
#         if(gen.getSeqLen() == 0):
#             gen.genSequence("RealLife")
#             io.reset()
#             gui.mistake.max = 1


#     # If user not on a game difficulty, unload sequence
#     if(gui.difficulty == "None"):
#         if(gen.getSeqLen() != 0):
#             gen.clearSeq()

#         io.reset()

#     # Else...
#     else:
#         if(gen.getSeqLen() > 0):
#             # Run first sequence, record if it is completed
#             completed = io.run_Sequence( gen.getAct() )

#             # Set the hint text
#             gui.hint.set_Text( gen.getHint() )

#             # Set mistake text
#             gui.mistake.set_Text( io.mistakes )

#     # If completed, go to next activity
#     if(completed):
#         gen.remAct()
#         completed = False

#     # Decide if the player won or lost
#     if(gui.game_over == 1):
#         if(gen.getSeqLen() == 0):
#             gui.game_over = 2

#         elif(gui.timer.end):
#             gui.game_over = 3

#         elif(gui.difficulty == "Medium" and io.mistakes == gui.mistake.max):
#             gui.game_over = 3
            
#         elif(gui.difficulty == "Hard" and io.mistakes == gui.mistake.max):
#             gui.game_over = 3

#         elif(gui.difficulty == "Real Life" and io.mistakes == gui.mistake.max):
#             gui.game_over = 3

#     window.update_idletasks()
#     window.update()

# # Clean up the hardware
# closeGame(io)
