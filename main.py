from Func import *
from pygame import *
from const import *
from Game import *
import os
import time

screen = display.set_mode((WIDTH,HEIGHT))

display.set_caption("Jetpack Joyride")
#display.set_icon(image.load('res/textures/icon.png'))
textures = {
	"character": [image.load(os.path.join('res','sprites','runningman.png')),
		          image.load(os.path.join('res','sprites','runningman2.png')),
		          image.load(os.path.join('res','sprites','jumpingman.png'))],
	"blast": [image.load(os.path.join('res','sprites','jetpack_bottom.png')),
		      image.load(os.path.join('res','sprites','jetpack_middle.png')),
		      image.load(os.path.join('res','sprites','jetpack_top.png'))]
}

snds = {}
fonts = {}

running = True
while running:
	currTime = 0
	clock = time.Clock()
	game = Game(character)
	game.run(screen, snds, textures, fonts)
quit()
