try:
	from graphics_lib import GraphWin
except:
	from .graphics_lib import GraphWin

class Game:
	def __init__(self, title, width, height):
		self.screen = GraphWin(title, width, height)

		self.scenes = {}
		self.on_scene = ""

	def addScene(self, name, scene):
		self.scenes[name] = scene

	def setScene(self, name):
		if(name in self.scenes.keys()):
			self._unloadScene()
			self.on_scene = name
			self._loadScene()

	def _loadScene(self):
		for item in self.scenes[self.on_scene].getItems():
			self.screen.addItem(item)

	def _unloadScene(self):
		self.screen.clearItems()

	def update(self):
		pass

	def run(self):
		while(self.screen.isOpen()):
			self.update()
			self.screen.redraw()