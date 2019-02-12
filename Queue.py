from LinkedList import Node
from LinkedList import LinkedList

class Queue(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
### HOW DO I CHECK TO SEE IF QUEUE IS EMPTY
    def isEmpty(self):
        if self.head == None and self.tail == None:
            empty = True
        else:
            empty = False
        return(empty)



    def enqueue(self,valueOfNode):
        #If the linkedlist is empty this makes the head and tail equal to the new node
        if self.isEmpty():
            n = Node(valueOfNode,None)
            self.head = n
            self.tail = n
        else:
            #if the linkedlist already has a node(s) you want to add to the tail
            n = Node(valueOfNode,None)
            self.tail.nextNode = n      # Adds to list
            self.tail = n

    def dequeue(self):
        if self.isEmpty():
            return(None)    #prevents an error if list is empty
        else:
            nodeToDequeue = self.head   #saves a copy of the node to dequeue
            if self.head.nextNode == None:  # checks if it is at end of list
                self.head,self.tail = None,None #resets list to empty if last node
            else:
                self.head = self.head.nextNode  #moves forward to next node
            return(nodeToDequeue)

    def peek(self):
        return(self.head.value) #shows the value of the next node to be dequeued




f = open('/Users/nicholasmaisel/Documents/Programming/Algorithms/magicitems.py',"r")
lines = list(f)
f.close

a = Queue()
for i in lines:
    a.enqueue(i)
    print(i)

print(a.head.nextNode)

while a.head != None:
    print(a.dequeue().valueOfNode)
