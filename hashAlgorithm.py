from LinkedList import LinkedList
from LinkedList import Node
import random

ARRAY_LENGTH = 255


class HashTable():
    def __init__(self,chainLength):
        self.chainLength = chainLength
        self.table = {}

    def hash(self,key):
        #Uses python's built in hash tool to and modding it to chainlength
        return(hash(key)%self.chainLength)
    
    
    def get(self,key):
        hashedKey = self.hash(key)
        flag = False
        
        #check to see if the key exists in the hash table
        if hashedKey in self.table.keys():
            curNode = self.table[hashedKey].firstNode
            while flag == False:
                if curNode.valueOfNode == key:
                    flag = True
                elif curNode.nextNode:
                    curNode = curNode.nextNode
                else:
                    break
        return(flag)


    def put(self,key):
        hashedKey = self.hash(key)
        if hashedKey in self.table.keys(): #Checks to see if the hash has been used
            self.table[hashedKey].AddToFront(key)
        else:
            #If there is not already a value mapped to this hash output's
            #Linked list, simply make one and set the key to the value of that
            #linked lists's firstNode value
            self.table[hashedKey] = LinkedList(key)
            



def main():
    b = HashTable(255)
    f = open('magicitems.txt',"r")
    magicitems = list(f)
    f.close
    magicitems = [x.strip() for x in magicitems]
    magicitems = [x.lower() for x in magicitems]
    magicitems = [x.replace(' ','') for x in magicitems]

    a = magicitems

    for i in a:
        b.put(i)




    TOTALCOMP = 0

    for i in range(100):
        rng = round(random.random()*255)
        print(rng)
        l, comparisons = b.get(list(b.table.keys())[rng])
        TOTALCOMP += comparisons

    print(TOTALCOMP/100)





main()
