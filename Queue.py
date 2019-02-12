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
            self.tail.nextNode = n
            self.tail = n

    def dequeue(self):
        if self.isEmpty():
            return(None)
            return(nodeToDequeue)
        else:
            nodeToDequeue = self.head
            if self.head.nextNode == None:
                self.head,self.tail = None,None
            else:
                self.head = self.head.nextNode
            return(nodeToDequeue)

    def peek(self):
        return(self.head.val)




a = Queue()
a.enqueue("John")
a.enqueue("Mitchell")
a.enqueue("laney")
a.enqueue("Dane")
a.enqueue("hellothere")

for i in range(0,5):
    print(a.dequeue().val, "##")
    i+= 1
