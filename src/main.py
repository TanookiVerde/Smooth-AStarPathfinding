from bspline import*
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
        pygame.draw.circle(DISPLAYSURF,color,points[i],5,0)
def DrawPath(points):
    for i in range(0,100):
        ponto = Interpolate(i/100.0,d,points,k,w) 
        temp = [int(ponto[0]),int(ponto[1])]
        pygame.draw.circle(DISPLAYSURF,(0,255,0),temp,2,0)

#ZONA DE TESTES
wi = [[1 for i in range(10)] for j in range(10)]
g = SquareGrid(10,10,wi)
start = (1,1)
goal = (7,8)
r = a_star_search(g,start,goal)
k = [1,1,1,2,3,4,5,6,7,8,9,10,11,12,12,12] #len(k) = len(p) + d + 1
w = [1,1,1,1,1,1,1,1,1,1,1,1,1] # len(w) = len(p)
d = 2
t = 0
v = [[0 for x in range(0,2)] for y in range(0,13)]
for i in range(0,10):
    for j in range(0,2):
        v[i][j] = r[i][j]*50
        
#NAO MEXE
DISPLAYSURF.fill((255,255,255))
DrawPath(v)
DrawPoints(v)

#MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

