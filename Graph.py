class Graph:
    def __init__(self):
        self.verticies = []
        self.edges = {} # Edges are represented as a dictionary, key = from val = to
        self.numVerticies = 0

    def addVertex(self,vid):
        self.verticies.append(vid)
        self.numVerticies += 1

    def addEdge(self,vertex1, vertex2):
        self.edges[vertex1] = vertex2
