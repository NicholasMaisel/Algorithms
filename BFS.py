from Queue import Queue
def BFS(graphList, target):
    target = int(target)-1
    Q = Queue()
    Q.enqueue(graphList[target]) # Takes the first Vertex and adds it to Queue
    graphList[target].marked = 1  # Marks target
    while Q.isEmpty != False:
        v = Q.dequeue()
        if v == None:
            break
        print(v.valueOfNode.vid)
        v.valueOfNode.marked = True
        for w in v.valueOfNode.adjList:
            if w.marked == False:
                w.marked = True
                Q.enqueue(w)
