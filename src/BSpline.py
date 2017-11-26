#//////////////////////////////////////////////////////////#
#ALUNO: PEDRO VITOR MARQUES NASCIMENTO                     #
#DRE: 116037448 TRABALHO: PROJETO FINAL DE CALCULO NUMERICO#
#//////////////////////////////////////////////////////////#
import pygame
from pygame.locals import*

class BSpline:
    def __init__(self,degree,points):
        self.degree = degree
        self.controlPoints = self.ConvertToGlobalPoints(points)
        self.knots = []
        self.controlPointColor = (255,0,0)
        self.splineColor = (0,255,0)
        self.Prepare()
    def Prepare(self):
        #Objetivo: Seta os knot values para repetirem no inicio e no final
        self.knots = [1 for i in range(0,len(self.controlPoints) + self.degree + 1)]
        for i in range(0,2):
            self.knots[i] = 1
        for i in range(2,len(self.knots)-3):
            self.knots[i] = i-1
        for i in range(len(self.knots)-3,len(self.knots)):
            self.knots[i] = len(self.knots)-4
    def Interpolate(self,t):
        #Objetivo: Interpola os pontos
        n = len(self.controlPoints)                                 #Descobre quantos pontos de controle existem
        dim = len(self.controlPoints[0])                            #Encontra quantas coordenadas tem a posicao
        dom = [self.degree, len(self.knots)-1-self.degree]          #Define qual o intervalo do parametro t
        low = self.knots[dom[0]]                                    #Define extremidade esquerda do intervalo
        high = self.knots[dom[1]]                                   #Define extremidade direita do intervalo
        t = t*(high-low)+low                                        #Coloca t de forma tal que facilmente se descubra em qual intervalo entre os knots esta
        for s in range(dom[0], dom[1]):                             #Indo de uma extremidade a outra   
            if t >= self.knots[s] and t <= self.knots[s+1]:         #Define qual segmento do intervalo t esta e guarda em s (onde o for para)
                break
        v = [[0 for x in range(0,dim+1)] for y in range(0,n)]
        for i in range(0,n):
            for j in range(0,dim):
                v[i][j] = self.controlPoints[i][j]                  #vetor V cujos valores iniciais sao as coordenadas dos pontos         
        alpha = 1
        for m in range(1,self.degree+1):
            for i in range(s,s-self.degree-1+m,-1):
                alpha = (t-self.knots[i])/(self.knots[i+self.degree+1-m]-self.knots[i]) #Calcula alpha
                for j in range(0,dim+1):
                    v[i][j]=(1-alpha)*v[i-1][j]+alpha*v[i][j]       #Calcula a funcao base utilizando valores ja calculados anteriormente no loop
        result = [0 for x in range(0,dim+1)]
        for j in range(0,dim):
            result[j] = v[s][j]                                     #Armazena o resultado em result[]
        return result
    def DrawPoints(self,surf):
        #Objetivo: Desenha pontos na tela
        if len(self.controlPoints) == 0:
            return
        for i in range(0,len(self.controlPoints)):
            temp = self.controlPoints[i]
            temp = (temp[0]+25,temp[1]+25)
            pygame.draw.circle(surf,self.controlPointColor,temp,5,0)
    def DrawPath(self,surf):
        #Objetivo: Desenha caminho interpolado na tela
        if len(self.controlPoints) == 0:
            return
        for i in range(1,300):
            ponto = self.Interpolate(i/300.0) 
            temp = [int(ponto[0])+25,int(ponto[1])+25]
            pygame.draw.circle(surf,self.splineColor,temp,5,0)
    def ConvertToGlobalPoints(self,points):
        #Objetivo: transforma coordenada da tabela em coordenada na tela
        p = []
        for next in points:
            p.append((next[0]*50,next[1]*50))
        return p
