from Queue import Queue
from Stack import Stack

def isPalindrome(magicitems):
    for item in magicitems:
        item = item.strip()
        item = item.replace(' ','')
        item = item.lower()

        palindrome = True
        a = Queue()
        b = Stack()

        for letter in item:
            a.enqueue(letter)
            b.push(letter)
            palindrome = True

        while not b.isEmpty() and not a.isEmpty():
            x = b.pop().valueOfNode
            w = a.dequeue().valueOfNode
            if x == w:
                pass
            else:
                palindrome = False
        if palindrome:
            print(item, " Plaindrome =", palindrome)







f = open('/Users/nicholasmaisel/Documents/Programming/Algorithms/magicitems.txt',"r")
magicitems = list(f)
f.close

print(isPalindrome(magicitems))
