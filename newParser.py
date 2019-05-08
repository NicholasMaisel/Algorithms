from vertex import Vertex
b = open("C:\\Users\\maristuser\\Desktop\\magicitems.txt")
def lineGenerator(b):
        yield(b.readline().strip().split(' '))
        
instruct = lineGenerator(b)
vertList = []
graphLists = []

def follow(instruct):
    graphid = -1
    while True:
        cur = next(instruct)
        while cur[0] == '--' or cur[0] == '':
            cur = next(instruct)
            
        if cur[0] == 'new':
            if len(vertList) == 0:
                pass
            else:
                graphList.append(vertList)
                vertList.clear() 
        if cur[0] == 'add':
            if cur[1] == 'vertex':
                vertList.append(Vertex(cur[2]))
            if cur[1] == 'edge':
                vertexDict[int(cur[2])-1].adjList.append(vertexDict[int(cur[4])-1])
                vertexDict[int(cur[4])-1].adjList.append(vertexDict[int(cur[2])-1])
                
                
