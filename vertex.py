class Vertex:
    def __init__(self,vid):
        self.vid = vid
        self.adjList = []
        self.marked = 0

    def addEdge(self, vid):
        self.adjList.append(vid) #adds vertex to the adjacency list
