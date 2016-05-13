from pygame import *
from random import *
from Func import *
import os

screen = display.set_mode((1024, 768))
boxx, boxy = 100,384
vy = 0
vx = 3
grav = 0.2
thrust = 0.3
frame = 0
xpos = 0
zap = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
stzappers = []
stzapperPos = []
temp = 0

def shakeImage(img,x,y):
    dx = [-1,0,1]
    dy = [-1,0,1]
    posx = x+dx[randint(0,2)]
    posy = y+dy[randint(0,2)]
    screen.blit(img,(posx,posy))

def getPos(img,upbound,downbound,x):
    return randint(downbound - img.get_height(), upbound)

    

pics = {
    'barry': [image.load(os.path.join('res','sprites','runningman.png')),
              image.load(os.path.join('res','sprites','runningman2.png')),
              image.load(os.path.join('res','sprites','jumpingman.png'))],
    
    'jetpack': [image.load(os.path.join('res','sprites','jetpack_bottom.png')),
              image.load(os.path.join('res','sprites','jetpack_middle.png')),
              image.load(os.path.join('res','sprites','jetpack_top.png'))],
    
    'backgrounds': [image.load(os.path.join('res','backgrounds','bg1.png')),
                    image.load(os.path.join('res','backgrounds','bg1.png'))],
    
    'szappers': [image.load(os.path.join('res','zappers','horizontal1.png')),
                 image.load(os.path.join('res','zappers','horizontal2.png')),
                 image.load(os.path.join('res','zappers','horizontal3.png')),
                 image.load(os.path.join('res','zappers','horizontal4.png')),
                 image.load(os.path.join('res','zappers','left-right1.png')),
                 image.load(os.path.join('res','zappers','left-right2.png')),
                 image.load(os.path.join('res','zappers','left-right3.png')),
                 image.load(os.path.join('res','zappers','left-right4.png')),
                 image.load(os.path.join('res','zappers','right-left1.png')),
                 image.load(os.path.join('res','zappers','right-left2.png')),
                 image.load(os.path.join('res','zappers','right-left3.png')),
                 image.load(os.path.join('res','zappers','right-left4.png')),
                 image.load(os.path.join('res','zappers','vertical1.png')),
                 image.load(os.path.join('res','zappers','vertical2.png')),
                 image.load(os.path.join('res','zappers','vertical3.png')),
                 image.load(os.path.join('res','zappers','vertical4.png'))]
                 
    }

running = True
myClock = time.Clock()

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    keys = key.get_pressed()
    if keys[27]: break
    screen.fill((0,0,0))
    if keys[K_SPACE]:
        vy -= thrust
    else:
        vy += grav
        
    if boxy+45 > 688 and vy > 0:
        vy = 0
    elif boxy-36 <= 0 and vy < 0:
        vy = 0
    else:
        boxy += vy
    if xpos <= -3082:
        xpos = 0
    else:
        xpos -= vx
    screen.blit(pics['backgrounds'][0],(xpos,0))
    if boxy < 708 and vy != 0 or boxy <= 34.5:
        if keys[K_SPACE]:
            screen.blit(pics['jetpack'][1], (boxx-43,boxy+45))
            shakeImage(pics['jetpack'][0],boxx-55,660)
            shakeImage(pics['jetpack'][2], boxx-55,boxy+40)
        #screen.blit(pics['barry'][2],(boxx-36,boxy-42))
        shakeImage(pics['barry'][2], boxx-36, boxy-42)
    else:
        if frame <=  7:
            screen.blit(pics['barry'][0], (64,602))#(boxx-36,boxy-42))
            frame += 1
        else:
            screen.blit(pics['barry'][1], (64,602))#(boxx-36,boxy-42))
            frame += 1
            if frame > 14:
                frame = 0
    if sample(zap,1) == 1:
        temp = pics[szappers][randint(0,15)]
        stzappers.append(temp)
        stzapperPos.append(1024,getPos(temp))
        
    for i in range (len(stzappers)):
        screen.blit(stzappers[i],stzapperPos[i])
        stzapperPos -= vx
    vx += 0.002
    
        
    display.flip()

    myClock.tick(80)                        
    
quit()
