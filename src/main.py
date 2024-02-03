from lib.classes.game import Game
from lib.classes.scene import Scene

from pathlib import Path

DIRS = Path(__file__).resolve().parent
ASSETS = DIRS / "lib/assets"

GAME = Game("Refusal Defusal", 1600, 900)

scene1 = Scene()
scene1.addImage(ASSETS / 'Logo.png', 50, 50)

scene2 = Scene()

GAME.addScene('scene1', scene1)
GAME.addScene('scene2', scene2)
GAME.setScene('scene1')

GAME.run()