#//////////////////////////////////////////////////////////#
#ALUNO: PEDRO VITOR MARQUES NASCIMENTO                     #
#DRE: 116037448 TRABALHO: PROJETO FINAL DE CALCULO NUMERICO#
#//////////////////////////////////////////////////////////#
import heapq

class PriorityQueue:
    #Modificacao da classe heap para mais simplicidade
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]
def Heuristic(a, b):
    #Objetivo: Retorna um valor que fica menor quanto mais proximo do alvo, b
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
def AStar(graph, start, goal):
    #Objetivo: Calcula menor caminho entre start e goal no grafo graph
    frontier = PriorityQueue()
    frontier.put(start, 0)
    cameFrom = {}                                                       #Dicionario que armazena o pai do no dado com key - no antes dele no caminho
    costSoFar = {}                                                      #Custo ate o momento de cada no
    cameFrom[start] = None                                              #Comeca vazio
    costSoFar[start] = 0                                                #Custo do no inicial e zero
    while not frontier.empty():                                         #Enquanto existir vertice nao visitado 
        current = frontier.get()                                        #Pega o vertice com menor custo
        if current == goal:                                             #Checa se ele e o alvo 
            break                                                        
        for next in graph.Neighbors(current):                           #Itera entre os vizinhos calculando seu custo
            new_cost = costSoFar[current] + graph.Cost(current, next)   
            if next not in costSoFar or new_cost < costSoFar[next]:     #Se o vizinho atual ainda teve custo calculado ou o custo for menor que vindo por outro caminho
                costSoFar[next] = new_cost                              #atualiza custo
                priority = new_cost + Heuristic(goal, next)             #calcula o custo do caminho ate o vizinho
                frontier.put(next, priority)                            #coloca o vizinho na lista dos nos nao visitados
                cameFrom[next] = current                                #diz de onde foi calculado o ultimo custo
    m = goal
    result = []
    while m != start:                                                   #Este loop armazena o caminho do inicio ao fim no vetor result
        result.append(m)
        m = cameFrom[m]
    result.append(start)
    return result                                                       #Retorna result[]