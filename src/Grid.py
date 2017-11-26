#//////////////////////////////////////////////////////////#
#ALUNO: PEDRO VITOR MARQUES NASCIMENTO                     #
#DRE: 116037448 TRABALHO: PROJETO FINAL DE CALCULO NUMERICO#
#//////////////////////////////////////////////////////////#
import pygame
from pygame.locals import*

PATH_COLOR = (0,150,150)
WALL_COLOR = (150,0,0)

CELL_SIZE = 50

class Grid:
    def __init__(self,lines,columns):
        self.l = lines
        self.c = columns
        self.tiles = {}
        self.obstacles = []
        for i in range(0,self.l):
            for j in range(0,self.c):
                self.tiles[(i,j)] = Node(i,j,CELL_SIZE,False)
    def DrawGrid(self,surf):
        #Objetivo: Chama a funcao de desenho em cada no
        for next in self.tiles:
            self.tiles[next].DrawNode(surf)
        return
    def InputHandler(self,ev):
        #Objetivo: Se o usuario clicar em um no ele vira normal/obstaculo
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                id = (pos[0]/CELL_SIZE,pos[1]/CELL_SIZE)
                self.tiles[id].OnClick(self)
    def IsNotWall(self,id):
        #Objetivo: Retorna True se o no nao eh uma parede
        return self.tiles[id].obstacle == False
    def IsWall(self,id):
        #Objetivo: Retorna True se o no eh uma parede
        return self.tiles[id].obstacle == True
    def InBounds(self,id):
        #Retorna True se no esta dentro da tabela
        (x,y) = id
        return 0 <= x < self.c and 0 <= y < self.l
    def Neighbors(self,id):
        #Objetivo: Retorna vizinhos validos
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
        results = filter(self.InBounds, results)
        results = filter(self.IsNotWall, results)
        return results
    def Cost(self,fromN,toN):
        return 1
    def GetObstacles(self):
        #Objetivo: Retorna os obstaculos
        r = filter(self.IsWall,self.tiles)
        self.obstacles = r
        return r

class Node:
    def __init__(self,i,j,size,obstacle):
        self.pos = (i,j)
        self.size = size
        self.obstacle = obstacle
    def DrawNode(self,surf):
        #Objetivo: Desenha o no na tela em forma de retangulo
        box = Rect(self.pos[0]*self.size,self.pos[1]*self.size,self.size,self.size)
        if self.obstacle == True:
            pygame.draw.rect(surf,WALL_COLOR,box,0)
        else:
            pygame.draw.rect(surf,(255,255,255),box,0)
            pygame.draw.rect(surf,PATH_COLOR,box,2)
        return
    def OnClick(self,grid):
        #Objetivo: Muda para normal/obstaculo
        self.obstacle = not self.obstacle
