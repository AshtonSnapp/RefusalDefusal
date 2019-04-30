#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 30 April 2019
# Changes: Main
#####################################################################


from hardware import hardware as hw
from graphics import gui
from logic import rhClasses as rohe
from random import randint

# A function to be called that safely closes everything down. Takes in a reference to a HardIO object.
def closeGame(hard_io):
	# Closing remarks to be printed when the game closes. Feel free to add your own strings!
	closingRemarks = ["Have an awesome day!", "May the force be with you.", "Thank you for playing!", "Exited with status code 0 - success!", "b a n a n a"]

	hard_io.destroy()

	print closingRemarks[randint(0, len(closingRemarks) - 1)]

	exit(0)