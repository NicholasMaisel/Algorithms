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


def mergeSort



'''
For the comparison count, I am getting 221,445 comparisons. We learned that
selection sort operates at O(n^2). Am i counting all comparisons?
Am i missing anything?'''




def main():

    #Reads magicitems file
    f = open('magicitems.txt',"r")
    magicitems = list(f)
    f.close
    magicitems = [x.strip() for x in magicitems]
    magicitems = [x.lower() for x in magicitems]
    magicitems = [x.replace(' ','') for x in magicitems]

    a = magicitems
    a,comparisonCount = selectionSort(a)
    for i in a:
        print(i)
    print("Comparisons: ", comparisonCount)


main()
