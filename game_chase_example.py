##Python2
##basic game that lasts 60 seconds using pygame to chase the point around the matrix
#startup

from astro_pi import AstroPi
import time
import pygame
from pygame.locals import *
import thread
import random
import time

points = 0
running = True
speed = float(4) #speed is set to 4 to start with and goes up
pygame.init()
pygame.display.set_mode((640, 480))
ap = AstroPi()
ap.clear()

#makes hte point being chased
def make_point():
    px = random.randint(0,7)
    py = random.randint(0,7)
    ap.set_pixel(px,py,[pr,pg,pb])
    if(px == x and py == y):
        make_point()

#moving dot
x = 0
y = 0
r = 255
g = 0
b = 0

#colour of the point being chased
pr =0
pg = 252
pb = 248


leftco = 1 # co-efficient for left movement, 1 for right, -1 for left
upco = 0 #co-efficient for the up movement, -1 for up and 1 for down

make_point()
start = time.time()
while running:
    x =x + leftco
    y = y + upco
    #stop the game crashing when it gets to the end of the screen, this could be changed to make it go past and start on the other side
    if(x < 0) : x = 0
    if(x > 7) : x = 7
    if(y < 0) : y = 0
    if(y > 7) : y = 7

    p = ap.get_pixel(x,y)
    #debugging info as setting 0, 255, 255 did not work
    #print p
'
    #check if the point has been collected
    if(p[0] == pr and p[1] == pg and p[2] == pb):
        #its a point!
        points = points + 1
        speed = speed + 1 # increase speed
        make_point() # make another point
        
    ap.set_pixel(x,y,r,g,b)
    time.sleep( float(1)/speed)
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       #change the  co-efficient depending on the key pressed , or exit the game
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                running = False
            if event.key==K_LEFT:
                leftco = -1
                upco = 0
            elif event.key==K_RIGHT:
                leftco = 1
                upco = 0
            elif event.key==K_UP:
                leftco = 0
                upco = -1
            elif event.key==K_DOWN:
                leftco = 0
                upco = 1
    ap.set_pixel(x,y,0,0,0)

    now = time.time()
    #game exits after 60 seconds
    if(now - start > 60):
        running = False;
if(running == False):
    print("Finished")

#show the score beofre the game ends    
ap.show_message("points: " + str(points),0.2,[r,g,b])
ap.clear()
pygame.quit ()
