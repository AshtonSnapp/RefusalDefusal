from Tkinter import *

# Game Class
class Game(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		img = "roboso_0.png"
		self.image = PhotoImage()

#####################

# Main Code Stuffs

WIDTH = 800
HEIGHT = 480

window = Tk()
g = Game(window)
g.play()

window.mainloop()

# DIFFICULTIES:
# - Control-Alt-Deletus (Easy) - 
# - Balanced (Medium) - 
# - Touhou (Hard) - 
# - Real Life (Obligitory Nightmare Mode) - ONE MISTAKE, THEN YER DED