from Queue import Queue
def Bfs(graphList, target):
    target = int(target)-1
    Q = Queue()
    Q.enqueue(graphList[target]) # Takes the first Vertex and adds it to Queue
    graphList[target].mark()  # Marks target
    while Q.isEmpty != False:
        v = Q.dequeue()
        if v == None:
            break
        print(v.valueOfNode.vid)
        v.valueOfNode.mark()
        for w in v.valueOfNode.adjList:
            if w.marked == False:
                w.mark()
                Q.enqueue(w)
