def swap(Arr, j, smallPosition):
    tempVar = Arr[j]
    Arr[j] = Arr[smallPosition]
    Arr[smallPosition] = tempVar
    return(Arr)

def selectionSort(A):
    comparisons = 0     #used to count the number of comparisons
    n = len(A)
    j = 0
    for j in range(j, n-1):
        smallPos = j
        for x in range(j+1, n):
            #increments comparisons each time one is done, it is before the
            # inequality, because the inequality may not always be true.
            comparisons += 1
            if A[x] < A[smallPos]:
                smallPos = x
        A = swap(A,j,smallPos)  # Calls the swap function
    return(A,comparisons)       # Returns tuple of the sorted list and # of comps

def merge1(left, right):
    tempArr = []
    #Makes sure there the elements are not 1 in length (they would already)
    #be sorted
    while(len(left) > 1 and len(right) > 1):
        if (left[0] > right[0]):
            tempArr.append(right[0])
            right = right[1:]
        else:
            tempArr.append(left[0])
            left = left[:1]
    while(len(left) >= 1):
        tempArr.append(left[0])
        left = left[1:]

    while(len(right) >= 1):
        tempArr.append(right[0])
        right = right[1:]

    return(tempArr)

# Merge1 A -> Array
#        p -> Start index of subarray to sort
#        q -> SplitPoint
#        r -> end index of subarray to sort
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    left,right = [],[]
    for i in range(0,n1):
        left[i] = A[p+i-1]
    for j in range(0,n2):
        right[j] = A[q+j]
    i = 1
    j = 1
    for k in range(p,r):
        if left[i] <= right[i]:
            A[k] = L[i]
            i =i+1
        else:
            A[k] = right[j]
            j = j+1


def mergeSort(A):
    comparisons = 0
    n = len(A)
    if (n <= 1):
        return(A)
    splitPoint = int(n/2)
    left = mergeSort(A[:splitPoint])
    right = mergeSort(A[splitPoint:])

    return(merge(left,right))



def insertionSort(A):
    for i in range(0,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and key < A[j]:
        #this 'waits' until the item is located at a place
        #that the value before it is less than the value
        #after it and inserts the key value at a[j+1]
            A[j+1] = A[j]
            j -= 1
            A[j+1] = key #inserts the value
    return(A)

def quickSort(A):


def main():

    #Reads magicitems file
    f = open('magicitems.txt',"r")
    magicitems = list(f)
    f.close
    magicitems = [x.strip() for x in magicitems]
    magicitems = [x.lower() for x in magicitems]
    magicitems = [x.replace(' ','') for x in magicitems]

    a = magicitems
    a = insertionSort(a)
    for i in a:
        print(i)
    #print("Comparisons: ", comparisonCount)


main()


import random
random.random()*666
