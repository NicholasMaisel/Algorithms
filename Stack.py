from LinkedList import Node
from LinkedList import LinkedList

class Stack(LinkedList):        #this inherits the Node class
    def __init__(self):
        self.top = None
        self.firstNode = None

#The isEmpty function is used to make sure, before the linkedlist is edited
#that the edit will cause no errors.
    def isEmpty(self):
        if self.top:
            empty = False
        else:
            empty = True
            return(empty)

    def push(self,valueOfNode):
        if self.isEmpty():
            n = Node(valueOfNode,None) #Creates a new node to be pushed
            n.nextNode = self.top      #links the new node to the list
            self.top = n               #Makes the new node the top of list for LIFO
        else:
            n = Node(valueOfNode,None)
            n.nextNode = self.top
            self.top = n


    def pop(self):
        if not self.isEmpty():         # Ensures an empty list isnt popped
            nodeToBePopped = self.top  # Makes a copy of the node to return
            self.top = self.top.nextNode   # Remove node from list by moving up
            return(nodeToBePopped)

'''
f = open('/Users/nicholasmaisel/Documents/Programming/Algorithms/magicitems.py',"r")
lines = list(f)
f.close

a = Stack()
for i in lines:
    a.push(i)
    print(i)



while a.top != None:
    print('###',a.pop().valueOfNode)'''
