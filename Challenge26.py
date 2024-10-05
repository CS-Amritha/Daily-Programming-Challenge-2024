from collections import defaultdict
class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)  
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self, node, visited, parent):
        visited[node] = True 
        for neighbor in self.graph[node]:
            if not visited[neighbor]: 
                if self.dfs(neighbor, visited, node):
                    return True
            elif parent != neighbor:  
                return True
        return False
    def has_cycle(self):
        visited = [False] * self.v 
        for i in range(self.v):
            if not visited[i]:
                if self.dfs(i, visited, -1): 
                    return True
        return False
v = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
g = Graph(v)
for u, v in edges:
    g.add_edge(u, v)
if g.has_cycle():
    print("true")
else:
    print("false")
