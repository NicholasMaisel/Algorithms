# A = read()

def swap(Arr, j, smallPosition):
    tempVar = Arr[j]
    Arr[j] = Arr[smallPosition]
    Arr[smallPosition] = tempVar
    return(Arr)


def selectionSort(A)
    n = len(A)
    j = 0
    for i in range(A, j):
        smallPos = j
        for i in range(j+1, n-1)
            if A[i] < A[smallPos]
    swap(A,j,smallPos)
