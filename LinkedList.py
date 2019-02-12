class Node():
    def __init__(self,valueOfNode,nextNode):
        self.valueOfNode = valueOfNode
        self.nextNode = nextNode

class LinkedList():
    def __init__(self,firstNode):
        self.firstNode = firstNode

    def AddToFront(self,valueOfNode):
        n = Node(valueOfNode, self.firstNode)
        self.firstNode = n
        n.valueOfNode = valueOfNode

    def TraverseToLastNode(self):   #This function is used to add nodes to the end in AddToEnd()
        n = self.firstNode
        while(n.nextNode):
            n = n.nextNode
        return(n)

    def AddToEnd(self,valueOfNode):
        last = self.TraverseToLastNode()    #This finds the last node so we can update nextNode of the last Node
        n = Node(valueOfNode,None)
        last.nextNode = n

    def isEmpty(self):
        if self.firstNode:
            empty = False
        else:
            empty = True
        return(empty)

f = open(sasda)
