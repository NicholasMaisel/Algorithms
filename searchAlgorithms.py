import random
from sortingAlgorithms import mergeSort

linearComparisons = 0
binaryComparisons = 0
individualBinary = 0
individualLinear = 0

def linearSearch(A, target):
    global linearComparisons
    global individualLinear
    location = 0 # Location is the index of comparison
    while location < len(A): # Ensures we dont go out of array
        individualLinear +=1 # Updates counters
        linearComparisons +=1
        if A[location] == target: # Compares values to target
            flag = True
            break # Stop if we find the target
        else:
            flag = False
        location +=1 # Move onto next index
    return(flag,)



def binarySearch(A,start,stop,target):
    global binaryComparisons # Gives method access to global var
    global individualBinary
    flag = False
    midpoint = int((start + stop)/2) # Sets midpoint to middle
    binaryComparisons += 1 # Updates counters
    individualBinary += 1
    if start > stop: # Makes sure we havent exhausted search       
        flag = False
    elif (A[midpoint] == target): # Compares target
        flag = True
        location = midpoint
    elif (target < A[midpoint]): # Searches lower 
        binarySearch(A,start, midpoint-1, target)   
    else: # Searches upper
        binarySearch(A, midpoint+1,stop,target)

    return(flag)


def main():
    f = open('magicitems.txt',"r")
    magicitems = list(f)
    f.close
    magicitems = [x.strip() for x in magicitems]
    magicitems = [x.lower() for x in magicitems]
    magicitems = [x.replace(' ','') for x in magicitems]
    
    a = mergeSort(magicitems)
    
    
    timesToCheck = 42
    randomItems = []
    for i in range(timesToCheck):
        randomItems.append(random.choice(a))
        
    for i in randomItems:
        global individualLinear
        linearSearch(a,i)
        print("Comparisons Linear Search: ", individualLinear)
        individualLinear = 0
        
    for i in randomItems:
        global individualBinary
        binarySearch(a,0,len(a),i)
        print("Comparisons Binary Search: ", individualBinary)
        individualBinary = 0
        

    print("-----------------------------------------------")
    print("Searching Algorithm  |      Comparisons     ")
    print("---------------------|-------------------------")
    print("Linear Search: ","     |    ", linearComparisons/timesToCheck)
    print("Bianry Search: ","     |    ", binaryComparisons/timesToCheck)
 

main()
