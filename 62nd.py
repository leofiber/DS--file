import queue

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for _ in range(nVertices)] for _ in range(nVertices)]

    def addEdge(self, v1, v2):
        if 0 <= v1 < self.nVertices and 0 <= v2 < self.nVertices:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1

    def __bfs(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while not q.empty():
            u = q.get()
            print(u, end=" ")
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and not visited[i]:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for _ in range(self.nVertices)]
        for i in range(self.nVertices):
            if not visited[i]:
                self.__bfs(i, visited)

    def removeEdge(self, v1, v2):
        if 0 <= v1 < self.nVertices and 0 <= v2 < self.nVertices:
            if not self.containsEdge(v1, v2):
                return
            self.adjMatrix[v1][v2] = 0
            self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        if 0 <= v1 < self.nVertices and 0 <= v2 < self.nVertices:
            return True if self.adjMatrix[v1][v2] > 0 else False
        return False

# Create a graph with 5 vertices
g = Graph(5)

# Add edges to the graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)

print("BFS Traversal:")
g.bfs()
