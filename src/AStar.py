import heapq

class SquareGrid:
    def __init__(self, width, height,weights):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    def passable(self, id):
        return id not in self.walls
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1),(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    m = goal
    result = []
    while m != start:
        m = came_from[m]
        result.append(m)
    return result

#ZONA DE TESTES
"""
w = [[1 for i in range(10)] for j in range(10)]
g = SquareGrid(10,10,w)
start = (1,1)
goal = (7,8)
r = a_star_search(g,start,goal)
"""