class Node():
    def __init__(self,val,nextNode):
        self.val = val
        self.nextNode = nextNode

class LinkedList():
    def __init__(self,name,firstNode):
        self.name = name
        self.firstNode = firstNode

    def AddToFront(self,val):
        n = Node(val, self.firstNode)
        self.firstNode = n
        n.val = val

    def TraverseToLastNode(self):
        n = self.firstNode
        while(n.nextNode):
            n = n.nextNode
        return(n)

    def AddToEnd(self,val):
        last = self.TraverseToLastNode()
        n = Node(val,None)
        last.nextNode = n


def main():
    myList = LinkedList("myList",None)
    myList.AddToFront("Mitchell")
    myList.AddToEnd("Nicholas")
    myList.AddToFront("Laney")
    myList.AddToFront("Dane")
    myList.AddToEnd("Sheila")

    currentNode = myList.firstNode

    while currentNode:
        print(currentNode.val)
        currentNode = currentNode.nextNode
main()
