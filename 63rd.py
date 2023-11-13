class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for _ in range(nVertices)] for _ in range(nVertices)]

    def addEdge(self, v1, v2):
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
        if not self.containsEdge(v1, v2):
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
# Create a graph with 5 vertices
g = Graph(5)

# Add edges to the graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)

print("DFS Traversal:")
g.dfs()

