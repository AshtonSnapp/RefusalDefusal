from lib.display.window import Window
from lib.display.scene import Scene

win = Window()

scene1 = Scene(win)
scene1.addImage(50, 50, 'lib/assets/Dad.png', 
	{
		'event_name' : '<Button-1>',
		'callback' : lambda self, e: self.setPos(e.x, e.y)
	})
scene1()

win()