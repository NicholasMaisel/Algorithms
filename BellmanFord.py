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

    def ShortestPath(self, G, src, v, emptyList =[]):
        ''' Finds the shortest path by following the predecessor values of
            each vertex '''
        if src == v:
            emptyList.append(src.vid)
        elif v.p == None:
            print("There is no path from:", src.vid, " to: ", v.vid)
        else:
            self.ShortestPath(self,src,v.p,emptyList)
            if v.vid != None:
                emptyList.append(v.vid)
        return(emptyList)



    def BellmanFord(self,src):
        src = self.verticies[int(src)-1]
        self.InitSingleSource(src)
        for vert in range(len(self.verticies)-1):
            for edge in self.wEdges:
                u,v = edge[0], edge[1]
                self.Relax(u,v)
        for edge in self.wEdges:    # check for negative weight cycles
            u,v = edge[0], edge[1]
            if v.d > u.d + self.wEdges[u,v]:
                print("Negative weight cycle detected.")
                return 1
        for vt in self.verticies:  # Print output
            print()
            print(f'Path from {src.vid} to {vt.vid} costs: {vt.d}; ', end = '')
            sPath = self.ShortestPath(self,src,vt,emptyList = [])
            for i in range(len(sPath)):
                if i != len(sPath)-1:
                    print(f' {sPath[i]} ⇒', end = '')
                else:
                    print(f' {sPath[i]}')



def main():
    graphs = []
    graph_index = -1

    for line in open('graph2.txt','r'):
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

    for g in graphs:
        print(f'\n\n---------- \nGraph {graphs.index(g)}\n----------')
        g.BellmanFord(1)



main()
