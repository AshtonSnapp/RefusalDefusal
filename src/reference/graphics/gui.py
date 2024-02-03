
if(__name__ == "__main__"): from graphics_lib import *
else:                       from .graphics_lib import *

from time import time, sleep
from random import randint
from json import load as LOAD
from pathlib import Path

DIRS = Path(__file__).resolve().parent
ASSETS = DIRS / "Assets"

#----[CLASSES]-------------------------------------------------------
# Game Class
class Game(GraphWin):
    
    FPS = 60

    def __init__(self, scrn_width=16*50, scrn_height=9*50):
        self.SCREEN_SIZE = (self.WIDTH, self.HEIGHT) = (scrn_width, scrn_height)

        super().__init__("Refusal Defusal", self.WIDTH, self.HEIGHT, autoflush=False)
        self._last_update = time()
        self._timer = 0
        self.setMouseHandler(self._mouseHandler)

        self.scenes = {}
        self.scene = ""

        self.buttons = []

    def loadScene(self, name, file):
        self.scenes[name] = LOAD(file)

    def displayScene(self, name, btn_funcs):
        scene = self.scenes.get(name)

        if(scene):
            self.scene = name
            self.clearItems()

            for btn in scene.get('buttons'):
                new = Button( btn['x'], btn['y'], btn['width'], btn['height'], btn['color'],
                              btn['text'], btn['font-size'], btn['font-color'] )

                new.setOnClick(btn_funcs[ btn['name'] ])

                self.addButton(new)

            for img in scene.get('images'):
                new = Photo( ASSETS / img['path'], img['x'], img['y'] )
                self.addItem(new)

    def getGameTime(self):
        return self._timer

    def addButton(self, btn):
        if(btn not in self.buttons):
            self.buttons.append(btn)
            self.addItem(btn)

    def remItem(self, item):
        if(self.hasItem(item)):
            item.undraw()
            super().delItem(item)

    def clearItems(self):
        for item in self.items[:]:
            self.remItem(item)

    def hasItem(self, item):
        return item in self.items

    def _mouseHandler(self, point):
        mx = point.getX()
        my = point.getY()

        for button in self.buttons[:]:

            p1x, p1y, p2x, p2y = button.getBoundingBox()
            if(mx < p1x or mx > p2x or my < p1y or my > p2y): continue

            button._onClick(button)

    def redraw(self):
        now = time()
        dt = now - self._last_update

        if(dt > 1/self.FPS):
            self._timer += dt

            self._last_update = now
            self.setBackground("black")
            super().redraw()

    # Setup GUI for main screen
    # def setupHomeScreen(self):
        

        # # Declare button specifics
        # button_width = 200
        # button_height = 60

        # # Create difficulty buttons
        # easy_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Easy", command=lambda:self.loadScreen(self.setupEasyMode))
        # easy_diff.place(width=button_width, height=button_height, x=0, y=HEIGHT-button_height)

        # medium_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Medium", command=lambda:self.loadScreen(self.setupMediumMode))
        # medium_diff.place(width=button_width, height=button_height, x=200, y=HEIGHT-button_height)

        # hard_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Hard", command=lambda:self.loadScreen(self.setupHardMode))
        # hard_diff.place(width=button_width, height=button_height, x=400, y=HEIGHT-button_height)

        # rl_diff = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Real Life", command=lambda:self.loadScreen(self.setupRLMode))
        # rl_diff.place(width=button_width, height=button_height, x=600, y=HEIGHT-button_height)

        # # Create about and help buttons
        # about = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="About", command=lambda:self.loadScreen(self.setupAbout))
        # about.place(width=button_width, height=button_height, x=0, y=0)

        # help = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", height=1, width=9, padx=5, text="Help", command=lambda:self.loadScreen(self.setupHelp))
        # help.place(width=button_width, height=button_height, x=300, y=0)

        # exitB = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Exit", command=lambda:self.loadScreen("EXIT"))
        # exitB.place(width=button_width, height=button_height, x=600, y=0)

    # # Setup GUI for easy mode
    # def setupEasyMode(self):
    #     Game.display = Frame(self, bg="white")
    #     self.master.title("Easy Mode")
    #     self.difficulty = "Easy"

    #     # Place character image
    #     Photo(Game.display, "/home/pi/Desktop/RefusalDefusal/src/graphics/Resources/Dad.png",\
    #         456, 427, 230, HEIGHT/2-60)

    #     # Create back button
    #     back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
    #     back.place(width=100, height=40, x=0, y=0)

    #     # Create hint box
    #     self.hint = Hint(Game.display)

    #     # Create mistake box
    #     self.mistake = Mistake(Game.display)

    #     # Create timer
    #     self.timer = Timer(Game.display)
    #     self.timer.set(120)
    #     self.timer.start()

    #     self.game_over = 1

    # # Setup GUI for medium mode
    # def setupMediumMode(self):
    #     Game.display = Frame(self, bg="white")
    #     self.master.title("Medium Mode")
    #     self.difficulty = "Medium"

    #     # Place character image
    #     Photo(Game.display, "/home/pi/Desktop/RefusalDefusal/src/graphics/Resources/Nervous_Guy.png",\
    #         456, 427, 150, HEIGHT/2-50)

    #     # Declare button specifics
    #     button_width = 400
    #     button_height = 40
    #     button_spacing = 15

    #     # Create back button
    #     back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
    #     back.place(width=100, height=40, x=0, y=0)

    #     # Create hint box
    #     self.hint = Hint(Game.display)

    #     # Create mistake box
    #     self.mistake = Mistake(Game.display)

    #     # Create timer
    #     self.timer = Timer(Game.display)
    #     self.timer.set(120)
    #     self.timer.start()

    #     self.game_over = 1

    # # Setup GUI for hard mode
    # def setupHardMode(self):
    #     Game.display = Frame(self, bg="white")
    #     self.master.title("Hard Mode")
    #     self.difficulty = "Hard"

    #     # Place character image
    #     Photo(Game.display, "/home/pi/Desktop/RefusalDefusal/src/graphics/Resources/Jamaican.png",\
    #         456, 427, 180, HEIGHT/2+10)

    #     # Declare button specifics
    #     button_width = 400
    #     button_height = 40
    #     button_spacing = 15

    #     # Create back button
    #     back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
    #     back.place(width=100, height=40, x=0, y=0)

    #     # Create hint box
    #     self.hint = Hint(Game.display)

    #     # Create mistake box
    #     self.mistake = Mistake(Game.display)

    #     # Create timer
    #     self.timer = Timer(Game.display)
    #     self.timer.set(90)
    #     self.timer.start()

    #     self.game_over = 1

    # # Setup GUI for IRL mode
    # def setupRLMode(self):
    #     Game.display = Frame(self, bg="white")
    #     self.master.title("Real Life Mode")
    #     self.difficulty = "Real Life"

    #     # Place character image
    #     Photo(Game.display, "/home/pi/Desktop/RefusalDefusal/src/graphics/Resources/Sergeant.png",\
    #         456, 427, 180, HEIGHT/2)

    #     # Declare button specifics
    #     button_width = 400
    #     button_height = 40
    #     button_spacing = 15

    #     # Create back button
    #     back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
    #     back.place(width=100, height=40, x=0, y=0)

    #     # Create hint box
    #     self.hint = Hint(Game.display)

    #     # Create mistake box
    #     self.mistake = Mistake(Game.display)

    #     # Create timer
    #     self.timer = Timer(Game.display)
    #     self.timer.set(60)
    #     self.timer.start()

    #     self.game_over = 1

    # # Setup GUI for the About Page
    # def setupAbout(self):
    #     Game.display = Frame(self, bg="white")
    #     self.master.title("About")
    #     self.difficulty = "None"

    #     # Declare button specifics
    #     button_width = 400
    #     button_height = 40
    #     button_spacing = 15

    #     # Create back button
    #     back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
    #     back.place(width=100, height=40, x=0, y=0)

    # # Setup GUI for the Help Page
    # def setupHelp(self):
    #     Game.display = Frame(self, bg="white")
    #     self.master.title("Help")
    #     self.difficulty = "None"

    #     # Declare button specifics
    #     button_width = 400
    #     button_height = 40
    #     button_spacing = 15

    #     # Create back button
    #     back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
    #     back.place(width=100, height=40, x=0, y=0)

    # def setupEnd(self):
    #     Game.display = Frame(self, bg="white")
    #     self.master.title("GAMEOVER")
    #     self.difficulty = "None"

    #     # Create back button
    #     back = Button(Game.display, font=(Game.FONT, Game.FONT_SIZE), activebackground="#AAA", bg="#CCC", fg="#F22", height=1, width=9, padx=5, text="Back", command=lambda:self.loadScreen(self.setupHomeScreen))
    #     back.place(width=100, height=40, x=0, y=0)

    #     # Display text
    #     text = Text(Game.display, height=1, width=9, font=(Game.FONT, 34, "bold"), relief="flat")
    #     text.place(x=WIDTH/2-125, y=HEIGHT/2-100)

    #     if(self.game_over == 2):
    #         text.insert("1.0", "YOU WIN")

    #     elif(self.game_over == 3):
    #         text.insert("1.0", "YOU LOSE")

    #     text.config(state=DISABLED)

    # # Start the game at the home screen
    # def play(self):
    #     self.loadScreen(self.setupHomeScreen)

    # # Clean the display, update the display, display the display
    # def loadScreen(self, setupFunc):
    #     # Stop the mainloop if exiting
    #     if(setupFunc == "EXIT"):
    #         self.running = False
    #         self.master.destroy()

    #     # Clear the screen and any events stored
    #     Game.display.destroy()
    #     self.events = [lambda:""]

    #     # Load next screen
    #     setupFunc()
    #     Game.display.pack(fill=BOTH, expand=1)

    # # Handle the timer
    # def handleTimer(self):
    #     self.timer.update()

    # # Run events stored in self.events
    # def update(self):
    #     if not(self.difficulty == "None" or self.difficulty == "Game Over"):
    #         if(self.game_over == 1):
    #             self.handleTimer()

    #         else:
    #             self.loadScreen(self.setupEnd)
    #             self.game_over = 0


class Photo(Image):
    def __init__(self, filename, x=0, y=0):
        super().__init__(Point(x, y), filename)

class Button:
    def __init__(self, x, y, width, height, color, text, font_size=24, font_color="white"):
        self.rect = Rectangle(Point(x, y), Point(x+width, y+height))
        self.rect.setFill(color)

        self.txt = Text(self.rect.getCenter(), text)
        self.txt.setSize(font_size)
        self.txt.setTextColor(font_color)

    def getBoundingBox(self):
        p1x, p1y = self.rect.getP1().getX(), self.rect.getP1().getY()
        p2x, p2y = self.rect.getP2().getX(), self.rect.getP2().getY()

        return p1x, p1y, p2x, p2y

    def draw(self, gwin):
        self.rect.draw(gwin)
        self.txt.draw(gwin)

    def undraw(self):
        self.rect.undraw()
        self.txt.undraw()

    def setOnClick(self, func):
        self._onClick = func

    def _onClick(self):
        pass

# class Hint(Text):

#     def __init__(self, master):
#         Text.__init__(self, master, height=5, width=25, relief="flat", wrap=WORD, font=("Helvetica", 12, "bold"))

#         self.place(x=WIDTH/2-100, y=HEIGHT-100)
#         self.state = DISABLED

#         self.text = ""

#     def set_Text(self, text):
#         self.config(state=NORMAL)
#         self.delete("1.0", END)
#         self.insert("1.0", text)
#         self.config(state=DISABLED)


# class Mistake(Text):
#     def __init__(self, master):
#         Text.__init__(self, master, height=2, width=15, relief="flat", wrap=WORD, font=("Helvetica", 14, "bold"))

#         self.place(x=WIDTH/2-75, y=HEIGHT/2)
#         self.state = DISABLED

#         self.text = ""
#         self.max = "inf"

#     def set_Text(self, text):
        
#         self.config(state=NORMAL)
#         self.delete("1.0", END)
#         self.insert("1.0", "MISTAKES: {}/{}".format(text, self.max))
#         self.config(state=DISABLED)


# class Timer(Text):

#     # Initialize the text widget
#     def __init__(self, master):
#         Text.__init__(self, master, height=1, width=5, relief="flat", font=("Helvetica", 34, "bold"))

#         # Place it centered in screen
#         self.place(x=WIDTH/2-50, y=HEIGHT/2-100)
#         self.state = DISABLED

#         # Initialize variables
#         self.duration = 0
#         self.remainder = 0
#         self.start_time = 0
#         self.end = False

#     # Set timer's duration, in seconds
#     def set(self, duration):
#     	self.duration = duration
#     	self.remainder = duration
#     	self.start_time = 0
#     	self.end = False

#     	# Display time
#     	formatted = self.formatTime()

#     	self.config(state=NORMAL)
#     	self.delete("1.0", END)
#     	self.insert("1.0", formatted)
#     	self.config(state=DISABLED)

#     # Update the timer
#     def update(self):
#         # Calculate what time is left
#         self.calculateTime()

#         # Format it
#         formatted = self.formatTime()

#         # Flash time if under 10s
#         if(self.remainder < 11):
#             if(int(formatted[3:]) % 2 == 0):
#                 self.config(fg="red")

#             else:
#                 self.config(fg="black")

#         # Display time
#         self.config(state=NORMAL)
#         self.delete("1.0", END)
#         self.insert("1.0", formatted)
#         self.config(state=DISABLED)

#     # Format time in mm:ss format
#     def formatTime(self):
#         pre_form = round(self.remainder / 60.0, 2)

#         minute = str(int(pre_form))
#         second = str(int((pre_form - int(minute)) * 60.0))

#         if(len(minute) < 2):
#             temp = minute
#             minute = "0" + temp

#         return "{}:{}".format(minute, second)

#     # Calculate what time is left
#     def calculateTime(self):
#         self.remainder = self.duration - (time() - self.start_time)

#         if(self.remainder < 0):
#             self.end = True
#             self.remainder = 0

#     # Start timer
#     def start(self):
#     	self.start_time = time()

#----[MAIN]----------------------------------------------------------


if(__name__ == "__main__"):
    from pathlib import Path
    ASSETS = Path(__file__).resolve().parent / "Assets"

    g = Game()

    homescreen = Photo(ASSETS / "Resources/Logo.png", 456, 256)
    btn = Button(50, 50, 175, 50, "blue", "Bitch", 24, "white")

    g.addItem(homescreen)
    g.addItem(btn)

    while(g.isOpen()):

        g.redraw()
