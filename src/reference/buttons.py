from random import choice

BUTTONS = {}

def home_play(self):
	colors = ['blue', 'green', 'red', 'grey', 'black', 'yellow']
	self.rect.setFill( choice(colors) )


BUTTONS['home'] = {
	'play' : home_play,
}