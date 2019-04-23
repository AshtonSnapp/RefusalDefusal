#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 22 April 2019
# Changes: Fixed the comments for setting up the different GUIs.
#####################################################################
from Tkinter import *

#----[CLASSES]-------------------------------------------------------
# Game Class
class Game(Frame):

	# Initialize the main frame and sub-frame
	def __init__(self, master):
		Frame.__init__(self, master)

		self.master = master

		self.pack(fill=BOTH, expand=1)

		Game.display = Frame(self)

	# Setup GUI for main screen
	def setupHomeScreen(self):
		Game.display = Frame(self)
		self.master.title("Home Screen")

		# Declare button specifics
		button_width = 200
		button_height = 60
		button_spacing = 25

		# Create difficulty buttons
		easy_x = 150
		easy_y = 70

		easy_diff = Button(Game.display, activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Easy", command=lambda:self.loadScreen(self.setupEasyMode))
		easy_diff.place(width=button_width, height=button_height, x=easy_x, y=easy_y)

		medium_diff = Button(Game.display, activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Medium", command=lambda:self.loadScreen(self.setupMediumMode))
		medium_diff.place(width=button_width, height=button_height, x=easy_x, y=easy_y+(button_height+button_spacing))

		hard_diff = Button(Game.display, activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Hard", command=lambda:self.loadScreen(self.setupHardMode))
		hard_diff.place(width=button_width, height=button_height, x=easy_x, y=easy_y+(button_height+button_spacing)*2)

		rl_diff = Button(Game.display, activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Real Life", command=lambda:self.loadScreen(self.setupRLMode))
		rl_diff.place(width=button_width, height=button_height, x=easy_x, y=easy_y+(button_height+button_spacing)*3)

		# Create about and help buttons
		about_x = 450
		about_y = 155

		about = Button(Game.display, activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="About", command=lambda:self.loadScreen(self.setupAbout))
		about.place(width=button_width, height=button_height, x=about_x, y=about_y)

		help = Button(Game.display, activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Help", command=lambda:self.loadScreen(self.setupHelp))
		help.place(width=button_width, height=button_height, x=about_x, y=about_y+button_height+button_spacing)

		exitB = Button(Game.display, activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Exit", command=lambda:exit(0))
		exitB.place(width=button_width, height=button_height, x=about_x, y=about_y+(button_height+button_spacing)*2)

	# Setup GUI for easy mode
	def setupEasyMode(self):
		Game.display = Frame(self)
		self.master.title("Easy Mode")

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	# Setup GUI for medium mode
	def setupMediumMode(self):
		Game.display = Frame(self)
		self.master.title("Medium Mode")

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	# Setup GUI for hard mode
	def setupHardMode(self):
		Game.display = Frame(self)
		self.master.title("Hard Mode")

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	# Setup GUI for IRL mode
	def setupRLMode(self):
		Game.display = Frame(self)
		self.master.title("Real Life Mode")

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	# Setup GUI for the About Page
	def setupAbout(self):
		Game.display = Frame(self)
		self.master.title("About")

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	# Setup GUI for the Help Page
	def setupHelp(self):
		Game.display = Frame(self)
		self.master.title("Help")

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	# Start the game at the home screen
	def play(self):
		self.loadScreen(self.setupHomeScreen)

	# Clean the display, update the display, display the display
	def loadScreen(self, setupFunc):
		Game.display.destroy()
		setupFunc()

		Game.display.pack(fill=BOTH, expand=1)

#----[MAIN]----------------------------------------------------------
# Setup window, originally 800x480
WIDTH = 800
HEIGHT = 480

window = Tk()
window.overrideredirect(1)
window.geometry("{}x{}".format(WIDTH, HEIGHT))

g = Game(window)
g.play()

window.mainloop()

# DIFFICULTIES:
# - Control-Alt-Deletus (Easy) - 
# - Balanced (Medium) - 
# - Touhou (Hard) - 
# - Real Life (Obligitory Nightmare Mode) - ONE MISTAKE, THEN YER DED
