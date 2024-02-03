try:
	from graphics_lib import Image, Point
	from extra_graphics import Button
except:
	from .graphics_lib import Image, Point
	from .extra_graphics import Button

class Scene:
	def __init__(self):
		self.imgs = []
		self.btns = []

	def addImage(self, path, x, y):
		img = Image(Point(x, y), path)
		self.imgs.append(img)

	def addButton(self, x, y, width, height, text, bg='blue', fg='white'):
		btn = Button(Point(x, y), Point(x+width, y+height), text, bg, fg)
		self.btns.append(btn)

	def getItems(self):
		items = []

		for img in self.imgs[:]:
			items.append(img)

		return self.items
