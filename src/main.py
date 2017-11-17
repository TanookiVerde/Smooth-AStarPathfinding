from BSpline import*
from AStar import*
from Grid import*

import pygame
from pygame.locals import*
import sys

S_WIDTH,S_HEIGHT = 500,500
pygame.init()

DISPLAYSURF = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Hello World!')
      
#GLOBAL || NAO MUDAR
DISPLAYSURF.fill((255,255,255))
gr = Grid(10,10)
start = (0,0)
goal = (9,9)
d = 2
r = []

#MAIN LOOP
while True:
    ev = pygame.event.get()
    for event in ev:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                gr.GetObstacles()
                r = a_star_search(gr,start,goal)
    gr.InputHandler(ev)
    gr.DrawGrid(DISPLAYSURF)
    if len(r) > 3:
        bs = BSpline(d,r)
        bs.DrawPoints(DISPLAYSURF)
        bs.DrawPath(DISPLAYSURF)
    pygame.display.update()
    DISPLAYSURF.fill((255,255,255))

