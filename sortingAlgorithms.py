from random import choice
# These variables are used to count the comparisons
# They are accessed globally in each sort function
quickComparisons = 0
mergeComparisons = 0
selectionComparisons = 0
insertionComparisons = 0

def swap(Arr, j, i):
    tempVar = Arr[j]
    Arr[j] = Arr[i]
    Arr[i] = tempVar
    return(Arr)

def selectionSort(A):
    global selectionComparisons # Used to count the number of comparisons
    n = len(A)
    for q in range(0, n-1):
        smallPos = q
        for x in range(q+1, n):
            # Increments comparisons each time one is done, it is before
            # the inequality, because the inequality may not always be true.
            selectionComparisons += 1
            if A[x] < A[smallPos]:
                smallPos = x
        A = swap(A,q,smallPos)  # Calls the swap function
    return(A) # Returns tuple of the sorted list and # of comps


def merge(left, right):
    global mergeComparisons
    sortedList=[] # Array used to store the sorted list
    i,j=0,0
    while i<len(left) and j<len(right): # Ensures we dont go out of list
        mergeComparisons +=1
        if left[i] < right[j]:          # Comparing the unitary lists
            sortedList.append(left[i])
            i+=1                        # Moves to next element in list
        else:
            sortedList.append(right[j])
            j+=1

    sortedList+=left[i:]
    sortedList+=right[j:]
    return (sortedList)

def mergeSort(A):
    n = len(A)
    if (n <= 1):
        return(A)
    splitPoint = int(n/2)
    # Defines left as a list with everything up to the splitpoint
    left = mergeSort(A[:splitPoint])
    right = mergeSort(A[splitPoint:])

    return(merge(left,right))

def insertionSort(A):
    global insertionComparisons # Comparison global variable access
    for i in range(0,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and key < A[j]: # Waits until key is greater than A[j]
            insertionComparisons +=1
            A[j+1] = A[j]
            j -= 1
            A[j+1] = key # Inserts the value
    return(A)



def quickSort(A):
    global quickComparisons
    left = []
    pivotList = []
    right = []
    if (len(A) <= 1):
        return(A)
    else:
        pivotPoint = choice(A)
        # The block below iterates over the lists and
        #chooses which partition values belong in
        for i in A:
            quickComparisons +=2
            if i < pivotPoint:
                left.append(i)
            elif i > pivotPoint:
                right.append(i)
            else:
                pivotList.append(i)
        leftSide = quickSort(left)
        rightSide = quickSort(right)
        return(leftSide + pivotList + rightSide)


def main():

    # Reads magicitems file
    f = open('magicitems.txt',"r")
    magicitems = list(f)
    f.close
    magicitems = [x.strip() for x in magicitems]
    magicitems = [x.lower() for x in magicitems]
    magicitems = [x.replace(' ','') for x in magicitems]
    a= magicitems
    b= magicitems


    sortingCalls =[insertionSort, selectionSort, mergeSort, quickSort]

    for algorithm in sortingCalls:
        algorithm.__call__(a)


    # QuickSort must be last because quickSort sorts in place!

    print("---------------------------------------------")
    print("Sorting Algorithm  |     Comparisons     ")
    print("-------------------|-------------------------")
    print("Insertion Sort: ","  |    ", insertionComparisons)
    print("Quick Sort: ","      |    ", quickComparisons)
    print("Merge Sort: ","      |    ", mergeComparisons)
    print("Selection Sort:","   |    ", selectionComparisons)
    print("---------------------------------------------")

main()
