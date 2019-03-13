from random import random
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
    global selectionComparisons    #used to count the number of comparisons
    n = len(A)
    j = 0
    for j in range(j, n-1):
        smallPos = j
        for x in range(j+1, n):
            #increments comparisons each time one is done, it is before the
            #inequality, because the inequality may not always be true.
            selectionComparisons += 1
            if A[x] < A[smallPos]:
                smallPos = x
        A = swap(A,j,smallPos)  # Calls the swap function
    return(A)       # Returns tuple of the sorted list and # of comps


def merge(left, right):
    global mergeComparisons 
    sortedList=[] #array to store the sorted list
    i,j=0,0
    while i<len(left) and j<len(right): # ensures we dont go out of list
        mergeComparisons +=1 
        if left[i] < right[j]:          # comparing the unitary lists
            sortedList.append(left[i])
            i+=1                        #Moves to next element in list
        else:
            sortedList.append(right[j])
            j+=1

    sortedList+=left[i:]
    sortedList+=right[j:]
    return (sortedList) #tupe of the list and the number of comps

def mergeSort(A):
    n = len(A)
    if (n <= 1):
        return(A)
    splitPoint = int(n/2)
    left = mergeSort(A[:splitPoint])    # makes left a list with everything up to the splitpoint
    right = mergeSort(A[splitPoint:])

    return(merge(left,right))





def insertionSort(A):
    global insertionComparisons         #used to count comparisons with global variable
    for i in range(0,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and key < A[j]:
            insertionComparisons +=1
        #this 'waits' until the item is located at a place
        #that the value before it is less than the value
        #after it and inserts the key value at a[j+1]
            A[j+1] = A[j]
            j -= 1
            A[j+1] = key #inserts the value
    return(A)

#The partition method is used to sort the sub arrays in place
def partition(A, left, right):
    i = left-1
    for j in range(left, right): #Iterates over each value in sub array
        if A[j] <= A[right]:
            i += 1
            A[j], A[i] = A[i], A[j]     #essentailly sways values of A[i] and a[j]
    A[i+1], A[right] = A[right], A[i+1]
    return (i+1)


def quickSort(A, left, right):
    global quickComparisons          #used to referenece the global variable comparisons
    if left < right:
        pivot = partition(A, left, right)   
        quickComparisons += (right - left)  #updates the global variable 
        quickSort(A, left, pivot-1)
        quickSort(A, pivot+1, right)
    return(A)


def main():

    #Reads magicitems file
    f = open('magicitems.txt',"r")
    magicitems = list(f)
    f.close
    magicitems = [x.strip() for x in magicitems]
    magicitems = [x.lower() for x in magicitems]
    magicitems = [x.replace(' ','') for x in magicitems]
    a= magicitems
   
    insertionSort(a)
    selectionSort(a)
    mergeSort(a)
    quickSort(a,0,len(a)-1) #quickSort must be last because quickSort sorts in place!!!!!
        
    print("---------------------------------------------")
    print("Sorting Algorithm  |     Comparisons     ")
    print("-------------------|-------------------------")
    print("Insertion Sort: ","  |    ", insertionComparisons)
    print("Quick Sort: ","      |    ", quickComparisons)
    print("Merge Sort: ","      |    ", mergeComparisons)
    print("Selection Sort:","   |    ", selectionComparisons)
    print("---------------------------------------------")

main()
