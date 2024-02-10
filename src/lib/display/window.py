from tkinter import Tk as ROOT

class Window:
	def __init__(self, title="Welcome", width=640, height=320):
		self.title = "Welcome"
		self.width = 640
		self.height = 320

		self._setup()

	def _setup(self):
		self._last_scene = None

		self._root = ROOT()
		self._root.resizable(False, False)
		self._root.title(self.title)

		self.resize(self.width, self.height)

	def getRoot(self):
		return self._root

	def resize(self, width, height):
		self.size = {'width':width, 'height':height}

		device_width = self._root.winfo_screenwidth()
		device_height = self._root.winfo_screenheight()

		center_x = int(device_width/2 - width/2)
		center_y = int(device_height/2 - height/2)

		self._root.geometry(f'{width}x{height}+{center_x}+{center_y}')

	def drawScene(self, scene):
		if(self._last_scene):
			self._last_scene.pack_forget()

		scene.pack()
		self._last_scene = scene

	def __call__(self):
		self._root.mainloop()
