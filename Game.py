from pygame import *
from Character import *
from time import *

class Game:
	score = 0
	hiscore = 0
	def __init__(self, character):
		self.character = character

	def run(self, screen, snds, textures, fonts):
		self.barry = barry = Character(self.character,barry,textures,snds)

		self.sounds = sounds
		self.textures = textures
		clock = time.Clock()

		self.barry.game = self

		running = True 
		while running:
			currTime = cTime()
			keys = key.get_pressed()

			for e in event.get():
				if e.type == QUIT:
					quit()
				if e.type == KEYDOWN:
					if e.key == K_ESCAPE:
						running = False
				# 	if e.key == K_SPACE:
				# 		self.propel()
			screen.fill((0,0,0))
			if keys[K_SPACE]:
				self.up = True
			self.move()

		display.flip()
		clock.tick(60)