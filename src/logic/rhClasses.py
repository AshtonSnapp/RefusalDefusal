#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 22 April 2019
# Changes: Basis for the Robot and Helper classes.
#####################################################################

class Robot(object):
	dialogue = {}  # A dictionary for storing dialogue for different states. Key is state ("calm", "angry", etc.), value is dialogue string.
	sprites = {}  # A dictionary for storing sprite images for different states (if we do it like that). Key is state, value is the path to the picture (or maybe an Image object?)

	def __init__(self, master):  # Don't know if master is needed, it's there just in case.
		self._state = "calm"  # Default State is Calm. Actual allowed states tbd in group meeting. Also, title case, all upper case, or all lower case?
		
		self._currentDialogue = dialogue[self._state]
		self._currentSprite = sprites[self._state]

		self._meter = 0  # Meter determines state. Keep it as low as possible! If it hits 100, you're screwed!

	@property
	def meter(self):
		return self._meter
	
	@meter.setter
	def meter(self, value):
		self._meter = value

	def updateState(self):
		# Don't know how exactly the meter will determine the state of the robot.

		self._currentDialogue = dialogue[self._state]
		self._currentSprite = sprites[self._state]


class Helper(object):
	dialogue = {}  # Dictionary of dictionaries. Stores different dialogue options for each helper. First key is the helper, second key is the action needed (flip, enter, pull), value is dialogue string.
	helpers = ["father", "drill_seargent", "cajun", "stoner420"]
	sprites = {}  # Dictionary of dictionaries. Stores different sprites for each helper. First key is the helper, second key is the action needed, value is the path to the picture (or maybe an Image object?)

	def __init__(self, master, sequence, difficulty):
		self.helper = helpers[difficulty]

		self._currentDialogue = dialogue[self.helper][sequence[0]]
		self._currentSprite = sprites[self.helper][sequence[0]]

	def updateState(self, robot):
		self._currentDialogue = dialogue[self.helper][sequence]
		self._currentSprite = sprites[self.helper][sequence]


# Have an awesome day. :banana: