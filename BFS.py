from Queue import Queue
def BFS(graphList, target):
    Q = Queue()
    index = 0
    Q.enqueue(graphList[target-1]) # Takes the first Vertex and adds it to Queue
    graphList[target-1].marked = 1  # Marks target
    
