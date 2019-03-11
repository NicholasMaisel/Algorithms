from random import random

def swap(Arr, i, j):
    Arr[i] = Arr[j]
    Arr[j] = Arr[i]
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

def merge(left, right):
    sortedList=[] #array to store the sorted list
    i,j=0,0
    while i<len(left) and j<len(right): # ensures we dont go out of list
        if left[i] < right[j]:          # comparint the unitary lists
            sortedList.append(left[i])
            i+=1                        #Moves to next element in list
        else:
            sortedList.append(right[j])
            j+=1

    sortedList+=left[i:]
    sortedList+=right[j:]
    return sortedList
def mergeSort(A):
    comparisons = 0
    n = len(A)
    if (n <= 1):
        return(A)
    splitPoint = int(n/2)
    left = mergeSort(A[:splitPoint])
    right = mergeSort(A[splitPoint:])

    return(merge1(left,right))

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

#The partition method is used to sort the sub arrays in place
def partition(A, left, right):
    i = left-1
    for j in range(left, right): #Iterates over each value in sub array
        if A[j] <= A[right]:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[right] = A[right], A[i+1]
    return i+1

def quickSort(A, left, right):
    if left < right:
        pivot = partition(A, left, right)
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

    a = magicitems
    a = quickSort(a,0,len(a)-1)
    for i in a:
        print(i)
    #print("Comparisons: ", comparisonCount)


main()
