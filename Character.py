from pygame import *
from const import *
from time import *


def __inti__(self, y, textures, snds):
	self.y = y

	# character sounds and textures
	self.textures = textures["character"][var] 
	self.blastTextures = textures["blast"]

	self.inAir = False
	self.dead = False

	self.charRect = Rect(CHARX-36,self.y-42,72,84)

	self.vy = 0
	self.vx = 10
	self.up = False
	self.down = False

	self.tokens = []
	self.coins = 0

def die(self):
	self.dead = True

def velocity(self):
	if self.up == True:
		self.vy -= .3
	elif self.down == True:
		self.vy += .3
	if self.y < 0 or self.y >= HEIGHT:
		vy = 0

def move(self):
	draw.circle(screen,(255,255,255),(CHARX, self.y+self.vy),5)


