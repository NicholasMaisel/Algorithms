from LinkedList import Node
from LinkedList import LinkedList

class Queue(LinkedList):
    def __init__(self):
        self.head = self.firstNode
        self.tail = None

    def enqueue(self,valueOfNode):
        if self.isEmpty():
            n = Node(valueOfNode)
            
