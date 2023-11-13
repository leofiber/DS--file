class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for _ in range(nVertices)] for _ in range(nVertices)]

    def addEdge(self, v1, v2):
        if 0 <= v1 < self.nVertices and 0 <= v2 < self.nVertices:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1

    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and not visited[i]:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for _ in range(self.nVertices)]
        self.__dfsHelper(0, visited)

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

g = Graph(5)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)

print("DFS Traversal:")
g.dfs()

print("Edge between 1 and 2:", g.containsEdge(1, 2))

g.removeEdge(1, 3)
g.dfs()
print("Edge between 1 and 3:", g.containsEdge(1, 3))
