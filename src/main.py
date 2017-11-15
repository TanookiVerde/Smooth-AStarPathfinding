from bspline import*
import pygame
import sys
from pygame.locals import*

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

def DrawPoints(points):
    color = (255,0,0)
    for i in range(0,len(points)):
        pygame.draw.circle(DISPLAYSURF,color,points[i],5,0)
def DrawPath():
    for i in range(0,100):
        ponto = Interpolate(i/100.0,d,p,k,w) 
        temp = [int(ponto[0]),int(ponto[1])]
        pygame.draw.circle(DISPLAYSURF,(0,255,0),temp,2,0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    DISPLAYSURF.fill((255,255,255))
    DrawPath()
    DrawPoints(p)

