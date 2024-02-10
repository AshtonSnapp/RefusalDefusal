from tkinter import PhotoImage

class Image:
	def __init__(self, scene, x, y, path):
		self.scene = scene
		self.x = x
		self.y = y
		self.path = path

	def load(self):
		self._img = PhotoImage(file=self.path)

		self._id = self.scene.create_image(
			(self.x, self.y),
			image=self._img
		)

	def unload(self):
		self.scene.delete(self._id)

	def setPos(self, x, y):
		self.x = x
		self.y = y

		self.scene.coords(self._id, self.x, self.y)

	def getPos(self):
		return self.x, self.y

	def on_event(self, event_name, callback):
		self.scene.tag_bind(
			self._id,
			event_name,
			lambda e: callback(self, e)
		)