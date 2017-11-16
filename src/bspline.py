def Interpolate(t,degree,points,knots,weights): 
    n = len(points)
    dim = len(points[0])
    dom = [degree,len(knots)-1-degree]
    low = knots[dom[0]]
    high = knots[dom[1]]
    t = t*(high-low)+low
    #Acha o segmento certo
    for s in range(dom[0],dom[1]):
        if t >= knots[s] and t<=knots[s+1]:
            break
    #Convertendo para coordenadas homogeneas
    v = [[0 for x in range(0,dim+1)] for y in range(0,n)]
    for i in range(0,n):
        for j in range(0,dim):
            v[i][j] = points[i][j]*weights[i]
        v[i][dim] = weights[i]
    #Interpola pontos 
    alpha = 1
    for m in range(1,degree+1):
        for i in range(s,s-degree-1+m,-1):
            alpha = (t-knots[i])/(knots[i+degree+1-m]-knots[i])
            for j in range(0,dim+1):
                v[i][j]=(1-alpha)*v[i-1][j]+alpha*v[i][j]
    #Converte de volta para coordenadas cartesianas
    result = [0 for x in range(0,dim+1)]
    for j in range(0,dim):
        result[j] = v[s][j]/v[s][dim]
    return result

#ZONA DE TESTES
"""
p = [[50,50],[100,50],[150,100],[150,150],[100,150],[50,100]]
k = [1,1,1,2,3,4,5,5,5] #len(k) = len(p) + d + 1
w = [1,1,1,1,1,1] # len(w) = len(p)
d = 2
t = 0

for i in range(0,100,1):
    print(Interpolate(i/100,d,p,k,w))
"""
