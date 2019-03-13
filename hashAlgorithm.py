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
        comparisons = 1     #Accounts for the 'get' part of each comparison
        hashedKey = self.hash(key)
        flag = False
        
        #check to see if the key exists in the hash table
        if hashedKey in self.table.keys():
            curNode = self.table[hashedKey].firstNode   #start out at the front
            while flag == False:  #only continue if we havent found the node we are looking for
                comparisons +=1
                if curNode.valueOfNode == key:
                    flag = True #if we found the key, this will break out of the while loop
                elif curNode.nextNode:
                    curNode = curNode.nextNode  #if we havent found it lets continue to the nextNode
                else:
                    break
        return(flag,comparisons)


    def put(self,key):
        hashedKey = self.hash(key)
        if hashedKey in self.table.keys(): #Checks to see if the hash has been used
            self.table[hashedKey].AddToFront(key)
        else:
            #If there is not already a value mapped to this hash output's
            #Linked list, simply make one and set the key to the value of that
            #linked lists's firstNode value
            self.table[hashedKey] = LinkedList(key)
            


# The main() function is used to find the average number of comparisons at any timesTo
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
        
    totalComparisons =0
    timesToCheck = 100
    for i in range(timesToCheck):
        found,comparisons = b.get(random.choice(magicitems))
        totalComparisons += comparisons
    
    print("Average Comparisons: ", totalComparisons/timesToCheck)
        
        
        
#This is used to run stuff only when not called via an import
#ie. if this module is being used as an import, main will not run
#however, if it is run directly, main() will be called
if __name__ == "__main__":
    main()
        
