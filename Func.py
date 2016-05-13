from pygame import *
from random import *

def shakeImage(img,x,y):
    dx = [-1,0,1]
    dy = [-1,0,1]
    posx = x+dx[randint(0,2)]
    posy = y+dy[randint(0,2)]
    screen.blit(img,(posx,posy))

