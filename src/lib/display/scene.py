from tkinter import Canvas

try:
	from image import Image
except:
	from .image import Image

class Scene(Canvas):

	def __init__(self, window):
		self.window = window
		super().__init__(self.window.getRoot(), **self.window.size, bg='black')

		self.imgs = {}

	def addImage(self, x, y, path, handler=None):
		img = Image(self, x, y, path)
		img.load()

		if(handler):
			img.on_event(**handler)

		self.imgs[img._id] = img

	def __call__(self):
		self.window.drawScene(self)