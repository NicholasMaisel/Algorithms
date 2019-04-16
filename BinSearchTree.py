from TreeNode import TreeNode

import random
class BSTree:
    def __init__(self):
        self.root = None

    def treeInsert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.insertTreeNode(self.root, val)

    def insertTreeNode(self,currentNode, val):
        if(val <= currentNode.vid):
            if(currentNode.left):
                self.insertTreeNode(currentNode.left, val)
            else:
                currentNode.left = TreeNode(val)

        elif(val > currentNode.vid):
            if(currentNode.right):
                self.insertTreeNode(currentNode.right, val)
            else:
                currentNode.right = TreeNode(val)

    def findInTree(self, val):
        return(self.findTreeNode(self.root,val))

    def findTreeNode(self, currentNode, val):
        if(currentNode == None):
            return(False)
        elif(val == currentNode.vid):
            return(True)
        elif(val < currentNode.vid):
            return(self.findTreeNode(currentNode.left, val))
        else:
            return(self.findTreeNode(currentNode.right, val))





def main():
    f = open('/Users/nicholasmaisel/Documents/Programming/Algorithms/magicitems.txt',"r")
    magicitems = list(f)
    f.close

    myTree = BSTree()
    for i in magicitems:
        myTree.treeInsert(i)


    randomItems = []
    for i in range(42):
        randomItems.append(random.choice(magicitems))

    for i in randomItems:
        myTree.findInTree(i)


main()



































def treeInsert(T, z):
    trailing = None
    current = T.root
    while(current!= None):
        trailing = current
        if(z.vid < current.vid):
            current = current.left
        else:
            current = current.right
    z.parent = trailing
    if(trailing == None):
        T.root = z
    else:
        if(z.vid < z.parent):
            x.parent.left = z
        else:
            z.parent.right = z
