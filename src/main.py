from bspline import*
from AStar import*
from grid import*
import pygame
import sys
from pygame.locals import*

S_WIDTH,S_HEIGHT = 500,500
pygame.init()

DISPLAYSURF = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Hello World!')

def DrawPoints(points):
    color = (255,0,0)
    for i in range(0,len(points)):
        print(points[i])
        pygame.draw.circle(DISPLAYSURF,color,points[i],5,0)
def DrawPath(points):
    for i in range(0,100):
        ponto = Interpolate(i/100.0,d,points,k,w) 
        temp = [int(ponto[0]),int(ponto[1])]
        pygame.draw.circle(DISPLAYSURF,(0,255,0),temp,2,0)

#NAO MEXE

DISPLAYSURF.fill((255,255,255))
gr = Grid(10,10)

print(gr.Neighbours((0,0)))

#MAIN LOOP
while True:
    ev = pygame.event.get()
    for event in ev:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    gr.InputHandler(ev)
    gr.DrawGrid(DISPLAYSURF)
    pygame.display.update()
    DISPLAYSURF.fill((255,255,255))

