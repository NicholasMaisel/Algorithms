from LinkedList import Node
from LinkedList import LinkedList

class Queue(LinkedList):
    def __init__(self):
        self.head = self.firstNode
        self.tail = None

    def enqueue(self,valueOfNode):
        if self.isEmpty():
            n = Node(valueOfNode,None)

    def dequeue(self):
        nodeToDequeue = self.head.nextNode
        self.head.nextNode = self.head
        return(nodeToDequeue)


a = Queue()
a.enqueue("Nicholas")
a.enqueue("Mitchell")
a.enqueue("laney")
a.enqueue("Dane")
a.enqueue("Sheila")
