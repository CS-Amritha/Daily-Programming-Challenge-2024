from collections import deque, defaultdict
class Graph:
    def __init__(self, v):
        self.v = v  
        self.graph = defaultdict(list)  
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def shortest_path(self, start, end):
        queue = deque([start])
        visited = [False] * self.v
        visited[start] = True
        parent = {start: None}
        while queue:
            node = queue.popleft()
            if node == end:
                return self._reconstruct_path(parent, start, end)
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
        return None
    def _reconstruct_path(self, parent, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse() 
        return path

v = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start = 0
end = 4
g = Graph(v)
for u, v in edges:
    g.add_edge(u, v)
shortest_path = g.shortest_path(start, end)
if shortest_path:
    print("Shortest Path:", shortest_path)
else:
    print("No path exists between the given nodes.")
