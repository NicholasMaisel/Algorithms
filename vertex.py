class Vertex:
    def __init__(self,vid, weight = 0):
        self.vid = vid
        self.adjList = []
        self.marked = 0
        self.weight = 0


    def addEdge(self, vid, weight = 0):
        self.adjList.append(vid) #adds vertex to the adjacency list

    def mark(self):
        self.marked = 1

    def unmark(self):
        self.marked = 0
