#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 1 May 2019
# Changes: Added timer to difficulties.
#####################################################################
from Tkinter import *
from time import time, sleep

#----[CLASSES]-------------------------------------------------------
# Game Class
class Game(Frame):
        FONT = "Verdana"
        FONT_SIZE = 12

        # Initialize the main frame and sub-frame
        def __init__(self, master):
                Frame.__init__(self, master)

                # Pack frame to the screen
                self.master = master
                self.pack(fill=BOTH, expand=1)

                # Create a subframe to be able to clear and update
                Game.display = Frame(self, bg="white")

                self.events = []
                self.running = True
                self.game_over = 0

                self.hint_text = ""

        # Setup GUI for main screen
        def setupHomeScreen(self):
                Game.display = Frame(self, bg="white")
                self.master.title("Home Screen")
                self.difficulty = "None"

                # Declare button specifics
                button_width = 200
                button_height = 60

                # Create difficulty buttons
                easy_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Easy", command=lambda:self.loadScreen(self.setupEasyMode))
                easy_diff.place(width=button_width, height=button_height, x=150, y=70)

                medium_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Medium", command=lambda:self.loadScreen(self.setupMediumMode))
                medium_diff.place(width=button_width, height=button_height, x=150, y=155)

                hard_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Hard", command=lambda:self.loadScreen(self.setupHardMode))
                hard_diff.place(width=button_width, height=button_height, x=150, y=240)

                rl_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Real Life", command=lambda:self.loadScreen(self.setupRLMode))
                rl_diff.place(width=button_width, height=button_height, x=150, y=325)

                # Create about and help buttons
                about = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="About", command=lambda:self.loadScreen(self.setupAbout))
                about.place(width=button_width, height=button_height, x=450, y=155)

                help = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Help", command=lambda:self.loadScreen(self.setupHelp))
                help.place(width=button_width, height=button_height, x=450, y=240)

                exitB = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Exit", command=lambda:self.loadScreen("EXIT"))
                exitB.place(width=button_width, height=button_height, x=450, y=325)

        # Setup GUI for easy mode
        def setupEasyMode(self):
                Game.display = Frame(self, bg="white")
                self.master.title("Easy Mode")
                self.difficulty = "Easy"

		# Create back button
		back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

		# Create hint box
		self.hint = Hint(Game.display)

		# Create timer
		self.timer = Timer(Game.display)
		self.timer.set(120)
		self.timer.start()

		self.game_over = 1

	# Setup GUI for medium mode
	def setupMediumMode(self):
		Game.display = Frame(self, bg="white")
		self.master.title("Medium Mode")
		self.difficulty = "Medium"

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

		# Create hint box
		self.hint = Hint(Game.display)

		# Create timer
		self.timer = Timer(Game.display)
		self.timer.set(120)
		self.timer.start()

		self.game_over = 1

	# Setup GUI for hard mode
	def setupHardMode(self):
		Game.display = Frame(self, bg="white")
		self.master.title("Hard Mode")
		self.difficulty = "Hard"

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

		# Create hint box
		self.hint = Hint(Game.display)

		# Create timer
		self.timer = Timer(Game.display)
		self.timer.set(90)
		self.timer.start()

		self.game_over = 1

	# Setup GUI for IRL mode
	def setupRLMode(self):
		Game.display = Frame(self, bg="white")
		self.master.title("Real Life Mode")
		self.difficulty = "Real Life"

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

		# Create hint box
		self.hint = Hint(Game.display)

		# Create timer
		self.timer = Timer(Game.display)
		self.timer.set(60)
		self.timer.start()

		self.game_over = 1

	# Setup GUI for the About Page
	def setupAbout(self):
		Game.display = Frame(self, bg="white")
		self.master.title("About")
		self.difficulty = "None"

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	# Setup GUI for the Help Page
	def setupHelp(self):
		Game.display = Frame(self, bg="white")
		self.master.title("Help")
		self.difficulty = "None"

		# Declare button specifics
		button_width = 400
		button_height = 40
		button_spacing = 15

		# Create back button
		back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

	def setupEnd(self):
		Game.display = Frame(self, bg="white")
		self.master.title("GAMEOVER")
		self.difficulty = "None"

		# Create back button
		back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
		back.place(width=100, height=40, x=0, y=0)

		# Display text
		text = Text(Game.display, height=1, width=13, font=(Game.FONT, 34, "bold"), relief="flat")
		text.place(x=WIDTH/2-125, y=HEIGHT/2-100)

		if(self.game_over == 2):
			text.insert("1.0", "YOU WIN")

		elif(self.game_over == 3):
			text.insert("1.0", "YOU LOSE")

		text.config(state=DISABLED)
		
                # Declare button specifics
                button_width = 400
                button_height = 40
                button_spacing = 15

                # Create back button
                back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
                back.place(width=100, height=40, x=0, y=0)

                # Create hint box
                self.hint = Hint(Game.display)

                # Create timer
                self.timer = Timer(Game.display)
                self.timer.set(120)
                self.timer.start()

                self.game_over = 1

        # Setup GUI for medium mode
        def setupMediumMode(self):
                Game.display = Frame(self, bg="white")
                self.master.title("Medium Mode")
                self.difficulty = "Medium"

                # Declare button specifics
                button_width = 400
                button_height = 40
                button_spacing = 15

                # Create back button
                back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
                back.place(width=100, height=40, x=0, y=0)

                # Create hint box
                self.hint = Hint(Game.display)

                # Create timer
                self.timer = Timer(Game.display)
                self.timer.set(120)
                self.timer.start()

                self.game_over = 1

        # Setup GUI for hard mode
        def setupHardMode(self):
                Game.display = Frame(self, bg="white")
                self.master.title("Hard Mode")
                self.difficulty = "Hard"

                # Declare button specifics
                button_width = 400
                button_height = 40
                button_spacing = 15

                # Create back button
                back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
                back.place(width=100, height=40, x=0, y=0)

                # Create hint box
                self.hint = Hint(Game.display)

                # Create timer
                self.timer = Timer(Game.display)
                self.timer.set(90)
                self.timer.start()

                self.game_over = 1

        # Setup GUI for IRL mode
        def setupRLMode(self):
                Game.display = Frame(self, bg="white")
                self.master.title("Real Life Mode")
                self.difficulty = "Real Life"

                # Declare button specifics
                button_width = 400
                button_height = 40
                button_spacing = 15

                # Create back button
                back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
                back.place(width=100, height=40, x=0, y=0)

                # Create hint box
                self.hint = Hint(Game.display)

                # Create timer
                self.timer = Timer(Game.display)
                self.timer.set(60)
                self.timer.start()

                self.game_over = 1

        # Setup GUI for the About Page
        def setupAbout(self):
                Game.display = Frame(self, bg="white")
                self.master.title("About")
                self.difficulty = "None"

                # Declare button specifics
                button_width = 400
                button_height = 40
                button_spacing = 15

                # Create back button
                back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
                back.place(width=100, height=40, x=0, y=0)

        # Setup GUI for the Help Page
        def setupHelp(self):
                Game.display = Frame(self, bg="white")
                self.master.title("Help")
                self.difficulty = "None"

                # Declare button specifics
                button_width = 400
                button_height = 40
                button_spacing = 15

                # Create back button
                back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
                back.place(width=100, height=40, x=0, y=0)

        def setupEnd(self):
                Game.display = Frame(self, bg="white")
                self.master.title("GAMEOVER")
                self.difficulty = "None"

                # Create back button
                back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
                back.place(width=100, height=40, x=0, y=0)

                # Display text
                text = Text(Game.display, height=1, width=13, font=(Game.FONT, 34, "bold"), relief="flat")
                text.place(x=WIDTH/2-125, y=HEIGHT/2-100)

                if(self.game_over == 2):
                    text.insert("1.0", "YOU WIN")

                elif(self.game_over == 3):
                    text.insert("1.0", "YOU LOSE")
                        
                text.config(state=DISABLED)

        # Start the game at the home screen
        def play(self):
                self.loadScreen(self.setupHomeScreen)

        # Clean the display, update the display, display the display
        def loadScreen(self, setupFunc):
                # Stop the mainloop if exiting
                if(setupFunc == "EXIT"):
                        self.running = False
                        self.master.destroy()

                # Clear the screen and any events stored
                Game.display.destroy()
                self.events = [lambda:""]

                # Load next screen
                setupFunc()
                Game.display.pack(fill=BOTH, expand=1)

        # Handle the timer
        def handleTimer(self):
                self.timer.update()

        # Run events stored in self.events
        def update(self):
                if not(self.difficulty == "None" or self.difficulty == "Game Over"):
                    if(self.game_over == 1):
                        self.handleTimer()

                    else:
                        self.loadScreen(self.setupEnd)
                        self.game_over = 0

	# Run events stored in self.events
	def update(self):
		if not(self.difficulty == "None" or self.difficulty == "Game Over"):
			if(self.game_over == 1):
				self.handleTimer()

			else:
				self.loadScreen(self.setupEnd)
				self.game_over = 0


class Hint(Text):

	def __init__(self, master):
		Text.__init__(self, master, height=5, width=25, relief="flat", wrap=WORD, font=("Helvetica", 12, "bold"))

		self.place(x=WIDTH/2-50, y=HEIGHT/2)
		self.state = DISABLED

		self.text = ""

	def set_Text(self, text):
		self.config(state=NORMAL)
		self.delete("1.0", END)
		self.insert("1.0", text)
		self.config(state=DISABLED)


class Timer(Text):

	# Initialize the text widget
	def __init__(self, master):
		Text.__init__(self, master, height=1, width=5, relief="flat", font=("Helvetica", 34, "bold"))

		# Place it centered in screen
		self.place(x=WIDTH/2-50, y=HEIGHT/2-100)
		self.state = DISABLED

		# Initialize variables
		self.duration = 0
		self.remainder = 0
		self.start_time = 0
		self.end = False

	# Set timer's duration, in seconds
	def set(self, duration):
		self.duration = duration
		self.remainder = duration
		self.start_time = 0
		self.end = False

		# Display time
		formatted = self.formatTime()

		self.config(state=NORMAL)
		self.delete("1.0", END)
		self.insert("1.0", formatted)
		self.config(state=DISABLED)

	# Update the timer
	def update(self):
		# Calculate what time is left
		self.calculateTime()

		# Format it
		formatted = self.formatTime()

		# Flash time if under 10s
		if(self.remainder < 11):
			if(int(formatted[3:]) % 2 == 0):
				self.config(fg="red")

			else:
				self.config(fg="black")

		# Display time
		self.config(state=NORMAL)
		self.delete("1.0", END)
		self.insert("1.0", formatted)
		self.config(state=DISABLED)

	# Format time in mm:ss format
	def formatTime(self):
		pre_form = round(self.remainder / 60.0, 2)

		minute = str(int(pre_form))
		second = str(int((pre_form - int(minute)) * 60.0))

		if(len(minute) < 2):
			temp = minute
			minute = "0" + temp

		if(len(second) < 2):
			temp = second
			second = "0" + second
		
		return "{}:{}".format(minute, second)

	# Calculate what time is left
	def calculateTime(self):
		self.remainder = self.duration - (time() - self.start_time)

		if(self.remainder < 0):
			self.end = True
			self.remainder = 0

	# Start timer
	def start(self):
		self.start_time = time()

#----[SETUP]---------------------------------------------------------
def setup():
	global WIDTH, HEIGHT

	# Setup window, originally 800x480
	WIDTH = 800
	HEIGHT = 480

	window = Tk()
	#window.overrideredirect(1)
	window.geometry("{}x{}".format(WIDTH, HEIGHT))

	return Game(window), window

#----[MAIN]----------------------------------------------------------
if(__name__ == "__main__"):
	# Setup the game
	g, window = setup()

	# Start the game
	g.play()

	# Main loop...
	while(g.running):
		g.update()
		window.update_idletasks()
		window.update()
		sleep(0.01)
