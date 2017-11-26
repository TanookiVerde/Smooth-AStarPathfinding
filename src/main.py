#//////////////////////////////////////////////////////////#
#ALUNO: PEDRO VITOR MARQUES NASCIMENTO                     #
#DRE: 116037448 TRABALHO: PROJETO FINAL DE CALCULO NUMERICO#
#//////////////////////////////////////////////////////////#

#############
#BIBLIOTECAS#
#############
import sys
import pygame
from pygame.locals import*
from BSpline import*
from AStar import*
from Grid import*

S_WIDTH,S_HEIGHT = 500,500

pygame.init()
mySurface = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("A* Pathfinding Smoothed - Pedro Nascimento (116037448)")
      
###################
#VARIAVEIS GLOBAIS#
###################
gr = Grid(10,10)
start = (0,0)
goal = (9,9)
d = 2
r = []
begin = False

#################
#FUNCOES GLOBAIS#
#################
def DrawOnUpdate():
    gr.InputHandler(ev)
    gr.DrawGrid(mySurface)
    if len(r)>3:
        bs = BSpline(d,r)
        bs.DrawPath(mySurface)
        bs.DrawPoints(mySurface)
def SearchPath():
    gr.GetObstacles()
    return AStar(gr,start,goal)

###########
#MAIN LOOP#
###########
while True:
    ev = pygame.event.get()             #lista de eventos
    for event in ev:                    #itera pelos eventos
        if event.type == QUIT:          #evento de "sair"
            pygame.quit()               #sair do programa
            sys.exit()
        if event.type == KEYDOWN:       #evento de "clique"    
            if event.key == K_SPACE:    #clique na tecla "espaco"
                r = SearchPath()        #acha menor caminho de A a B e o armazena em r
    DrawOnUpdate()                      #plota na tela a tabela, o caminho e os pontos
    pygame.display.update()
    mySurface.fill((255,255,255))

