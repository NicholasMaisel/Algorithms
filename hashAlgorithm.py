import LinkedList

ARRAY_LENGTH = 255


class HashTable():
    def __init__(self,chainLength):
        self.chainLength = chainLength
        self.table = {}

    def hash(key):
        return(key%chainLength)

    def get(key):
        flag = False
        hashedKey = self.hash(key)
        #See if hash table has a value at hashed index
        if hashedKey in self.table.values:
            selectedLList  = self.table[self.hash(key)] #grabs the linked list to search for element.
            if selectedLList.firstNode.valueOfNode == key:
                return(key)
            else:
                curNode = selectedLList.firstNode.nextNode
                # Runs thru the linked list checking if curNode.valueOfNode = key
                while curNode.ValueOfNode != key:
                    if curNode.nextNode: #If the current node has a next node, set CurNode equal to it
                        curNode = curNode.nextNode
                    else:
                        break   #if there isnt a next node break out and move on
                if curNode.valueOfNode == key: #ensures that the curNodes value is the value we are looking for
                    flag = True
        else:
            flag = False

        return(flag)

    def put(key):
        hashedKey = self.hash(key)
        if hashedKey in self.table.values:
            self.table[hashedKey].addToFront(key)
        else:
            #If there is not already a value mapped to this hash output's
            #Linked list, simply make one and set the key to the value of that
            #linked lists's firstNode value
            selt.table[hashedKey] = LinkedList(key)


def main():
    myHashTable = HashTable(ARRAY_LENGTH)
