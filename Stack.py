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
        if self.isEmpty():
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
            nodeToBePopped = self.top
            self.top = self.TraverseToNewTop() # Sets the new top
            self.top.nextNode = None      # Sets the top nextNode val to None
            return(nodeToBePopped)
