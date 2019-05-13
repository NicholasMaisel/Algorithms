class Vertex():
    def __init__(self,vid):
        self.vid = vid
        self.d = 0
        self.p = None

class Graph():
    def __init__(self):
        self.verticies = []
        self.wEdges = {}

    def addEdge(self,u,v,w):
        self.wEdges[u,v] = w


    def InitSingleSource(self,src):
        #src = self.verticies[int(src)]
        for vert in self.verticies:
            vert.d = float('Inf')
            vert.p = None
        src.d = 0

    def Relax(self,u,v):
        if v.d > u.d + self.wEdges[u,v]:
            v.d = u.d + self.wEdges[u,v]
            v.p = u

    def ShortestPath(self, G, src, v):
        if src == v:
            print(src.vid)
        elif v.p == None:
            print("There is no path from:", src.vid, " to: ", v.vid)
        else:
            self.ShortestPath(self,src,v.p)
            if v.vid != None:
                print(v.vid)


    def BellandFord(self,src):
        src = self.verticies[int(src)-1]
        self.InitSingleSource(src)
        for vert in range(len(self.verticies)-1):
            for edge in self.wEdges:
                u,v = edge[0], edge[1]
                self.Relax(u,v)
        for edge in self.wEdges:
            u,v = edge[0], edge[1]
            if v.d > u.d + self.wEdges[u,v]:
                print("Negative weight cycle detected.")
                return 0
        for vt in self.verticies:
            print()
            print('Path from',src.vid, '-->', vt.vid, 'costs:', vt.d)
            self.ShortestPath(self,src,vt)




def main():
    graphs = []
    graph_index = -1


    for line in open('/Users/nicholasmaisel/Documents/Programming/Algorithms/graph2.txt','r'):
        line = line.rstrip().split(' ')
        if '' in line:
            line.remove('')

        if graphs:
            currentGraph = graphs[graph_index]

        if line != []:
            if line[0] != '--':
                if line[0] == 'new':
                    graphs.append(Graph())
                    graph_index += 1
                    currentGraph = graphs[graph_index]
                elif line[0] == 'add':
                    if line[1] == 'vertex':
                        currentGraph.verticies.append(Vertex(int(line[2])))
                    if line[1] == 'edge':
                        u = currentGraph.verticies[int(line[2])-1]
                        v = currentGraph.verticies[int(line[4])-1]
                        w = int(line[5])
                        currentGraph.addEdge(u,v,w)
        else:
            pass


    print(graphs[0].BellandFord(1))


main()
