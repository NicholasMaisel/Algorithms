from Queue import Queue
from Stack import Stack

def isPalindrome(magicitems):
for item in magicitems:
    item = item.strip()
    item = item.lower()
    palindrome = True
    a = Queue()
    b = Stack()
    for letter in item:
        a.enqueue(letter)
        b.push(letter)

    while not b.isEmpty():
        if a.dequeue() == b.pop():
            pass
        else:
            palindrome = False
            return(palindrome)
        return(palindrome)



f = open('/Users/nicholasmaisel/Documents/Programming/Algorithms/magicitems.py',"r")
magicitems = list(f)
f.close
