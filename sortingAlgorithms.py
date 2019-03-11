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



def merge(left, right):
    tempArr = []
    #Makes sure there the elements are not 1 in length (they would already)
    #be sorted
    while(len(left) >= 1 and len(right) >= 1):
        print(left)
        print(right)
        if (left[0] > right[0]):
            tempArr.append(right[0])
            right = right[1:]
        else:
            tempArr.append(left[0])
            print("k")
            left = left[:1]
    while(len(left) >= 1):
        tempArr.append(left[0])
        left = left[1:]

    while(len(right) >= 1):
        tempArr.append(right[0])
        right = right[1:]

    return(tempArr)




def mergeSort(A):
    comparisons = 0
    n = len(A)
    print(n)
    if (n <= 1):
        return(A)
    splitPoint = int(n/2)
    left = mergeSort(A[:splitPoint])
    right = mergeSort(A[splitPoint:])

    return(merge(left,right))




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
