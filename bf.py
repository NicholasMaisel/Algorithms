class Vertex():
    def __init__(self,vid):
        self.vid = vid
        self.d = 0
        self.p = None

class Graph():
    def __init__(self):
        self.verticies = []
        self.wEdges = {}

    def addEdge(u,v,w):
        self.wEdges[[u,v]] = w


    def InitSingleSource(src):
        for vert in self.verticies:
            vert.d = float('Inf')
            vert.p = None
        self.src.d = 0


    def Relax(u,v):
        if v.d > u.d + self.wEdges[u,v]:
            v.d = u.d + self.wEdges[u,v]
            v.p = u

    def BellandFord(self,w,src):
        src = self.verticies[src]
        self.InitSingleSource(src)
        for vert in range(len(self.verticies)-1):
            for edge in self.wEdges:
                u,v = list(self.wEdges)[0], list(self.wEdges)[1]
                self.Relax(u,v)
        for edge in self.wEdges:
            u,v = list(self.wEdges)[0], list(self.wEdges)[1]
            if v.d > u.d + self.wEdges[u,v]:
                return 0
            return 1
