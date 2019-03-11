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


def mergeSort(A):
    comparisons = 0
    n = len(A)
    if (n <= 1):
        return(A,comparisons)
    splitPoint = int(n/2)
    left = mergeSort(A[:splitPoint])
    right = mergeSort(A[splitPoint:])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            print("i= ",i,"j= ",j,"k= ",k)
            A[k] = left[i]
            i += 1
        else:
            print("i= ",i,"j= ",j,"k= ",k)
            A[k] = right[j]
            j +=1
        k +=1

        while i < len(left):
            print("i= ",i,"j= ",j,"k= ",k)
            A[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            print("i= ",i,"j= ",j,"k= ",k)
            A[k] = right[i]
            j +=1
            k +=1

    return(A)



def insertionSort(A):
    pass


def quickSort(A):
    pass




def main():

    #Reads magicitems file
    f = open('magicitems.txt',"r")
    magicitems = list(f)
    f.close
    magicitems = [x.strip() for x in magicitems]
    magicitems = [x.lower() for x in magicitems]
    magicitems = [x.replace(' ','') for x in magicitems]

    a = magicitems
    a = mergeSort(a)
    for i in a:
        print(i)
    #print("Comparisons: ", comparisonCount)


main()
