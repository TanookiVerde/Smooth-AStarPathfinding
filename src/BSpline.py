import pygame
from pygame.locals import*

class BSpline:
    def __init__(self,degree,points):
        self.degree = degree
        self.controlPoints = self.ConvertToGlobalPoints(points)
        self.knots = []
        self.weights = []
        self.controlPointColor = (255,0,0)
        self.splineColor = (0,255,0)
        self.Prepare()
    def Prepare(self):
        self.knots = [1 for i in range(0,len(self.controlPoints) + self.degree + 1)]
        for i in range(0,3):
            self.knots[i] = 1
        for i in range(3,len(self.knots)-3):
            self.knots[i] = i-2
        for i in range(len(self.knots)-3,len(self.knots)):
            self.knots[i] = len(self.knots)-4
        self.weights = [1 for i in range(0,len(self.controlPoints))]
    def Interpolate(self,t):
        n = len(self.controlPoints)
        dim = len(self.controlPoints[0])
        dom = [self.degree, len(self.knots)-1-self.degree]
        low = self.knots[dom[0]]
        high = self.knots[dom[1]]
        t = t*(high-low)+low
        #Acha o segmento certo
        for s in range(dom[0], dom[1]):
            if t >= self.knots[s] and t <= self.knots[s+1]:
                break
        #Convertendo para coordenadas homogeneas
        v = [[0 for x in range(0,dim+1)] for y in range(0,n)]
        for i in range(0,n):
            for j in range(0,dim):
                v[i][j] = self.controlPoints[i][j]*self.weights[i]
            v[i][dim] = self.weights[i]
        #Interpola pontos 
        alpha = 1
        for m in range(1,self.degree+1):
            for i in range(s,s-self.degree-1+m,-1):
                alpha = (t-self.knots[i])/(self.knots[i+self.degree+1-m]-self.knots[i])
                for j in range(0,dim+1):
                    v[i][j]=(1-alpha)*v[i-1][j]+alpha*v[i][j]
        #Converte de volta para coordenadas cartesianas
        result = [0 for x in range(0,dim+1)]
        for j in range(0,dim):
            result[j] = v[s][j]/v[s][dim]
        print(result)
        return result
    def DrawPoints(self,surf):
        if len(self.controlPoints) == 0:
            return
        for i in range(0,len(self.controlPoints)):
            pygame.draw.circle(surf,self.controlPointColor,self.controlPoints[i],5,0)
    def DrawPath(self,surf):
        if len(self.controlPoints) == 0:
            return
        for i in range(1,200):
            ponto = self.Interpolate(i/200.0) 
            temp = [int(ponto[0]),int(ponto[1])]
            pygame.draw.circle(surf,self.splineColor,temp,2,0)
    def ConvertToGlobalPoints(self,points):
        p = []
        for next in points:
            p.append((next[0]*50,next[1]*50))
        print(p)
        return p

"""
p = [[50,50],[100,50],[150,100],[150,150],[100,150],[50,100]]
k = [1,1,1,2,3,4,5,5,5] #len(k) = len(p) + d + 1
w = [1,1,1,1,1,1] # len(w) = len(p)
d = 2
t = 0

for i in range(0,100,1):
    print(Interpolate(i/100,d,p,k,w))
"""
