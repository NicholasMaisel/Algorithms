
#The Node class is used as the objects for each element in the Linked list
# It keeps track of what value each node holds and what the nextNode in the list
class Node():
    def __init__(self,valueOfNode,nextNode):
        self.valueOfNode = valueOfNode
        self.nextNode = nextNode

class LinkedList():
    def __init__(self,firstNode):
        self.firstNode = firstNode

    def isEmpty(self):
        if self.firstNode:
            empty = False
        else:
            empty = True
        return(empty)

    def AddToFront(self,valueOfNode):
        if self.isEmpty():
            n = Node(valueOfNode, None) #Creates new node to be added to list.
            n.nextNode = self.firstNode #Adds node to the list, attaching at front.
            self.firstNode = n          #Makes new node the first node
            n.valueOfNode = valueOfNode #sets the value of the new node

        else:
            n = Node(valueOfNode, self.firstNode)
            n.nextNode = self.firstNode
            self.firstNode = n
            n.valueOfNode = valueOfNode


    def TraverseToLastNode(self):   #This function is used to add nodes to the end in AddToEnd()
        n = self.firstNode
        while(n.nextNode):
            n = n.nextNode
        return(n)

    def AddToEnd(self,valueOfNode):
        if self.isEmpty():
            n = Node(valueOfNode, None)
            self.firstNode = n
            n.valueOfNode = valueOfNode
        else:
            last = self.TraverseToLastNode()    #This finds the last node so we can update nextNode of the last Node
            n = Node(valueOfNode,None)
            last.nextNode = n



f = open('/Users/nicholasmaisel/Documents/Programming/Algorithms/magicitems.py',"r")
lines = list(f)
f.close

a = LinkedList(None)
for i in lines:
    a.AddToEnd(i)
    print(i)

print(a.firstNode.nextNode)

while a.firstNode != None:
    print('###',a.firstNode.valueOfNode)
    a.firstNode = a.firstNode.nextNode
