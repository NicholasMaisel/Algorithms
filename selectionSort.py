# A = read()

def swap(Arr, j, smallPosition):
    tempVar = Arr[j]
    Arr[j] = Arr[smallPosition]
    Arr[smallPosition] = tempVar
    return(Arr)


def selectionSort(A):
    n = len(A)
    j = 0
    for j in range(j, n-2):
        smallPos = j
        for x in range(j+1, n):
            if A[x] < A[smallPos]:
                smallPos = x
                print("smallPos = ",smallPos)
        A = swap(A,j,smallPos)
    return(A)


def main():
    a = [1,3,5,2,4,2,4553,234,2355,262,342,245234,2245,23523,52]
    selectionSort(a)
    print(a)


main()
