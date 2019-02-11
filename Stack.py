from LinkedList import Node
from LinkedList import LinkedList

class Stack(LinkedList):        #this inherits the Node class
    def __init__(self):
        self.top = None
        self.firstNode = None

    def isEmpty(self):
        if self.firstNode:
            empty = False
        else:
            empty = True
        return(empty)

    def push(self,valueOfNode):
        if isEmpty():
            n = Node(valueOfNode,None)
            self.firstNode = n
            self.top = n
        else:
            n = Node(valueOfNode,None)
            self.top.nextNode = n
            self.top = n

    def TraverseToNewTop(self):
        n = self.firstNode
        while(n.nextNode != self.top):
            n = n.nextNode
        return(n)


    def pop(self):
        if not self.isEmpty():
            poppedNode = N.top
            self.top = TraverseToNewTop()
            self.top.nextNode = None
            return(poppedNode)


a = Stack()
a.push("")
