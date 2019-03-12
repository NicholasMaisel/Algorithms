from random import random

def linearSearch(A, target):
    location = 0             # Location *is* the comparison count in this instance
    while location < len(A): #COMP
        if A[location] == target:
            flag = True
            break
        else:
            flag = False
        location +=1

    if flag == False:
        location = -1
    return(flag,location)


def binarySearch(A,start,stop,target):
    flag = False
    midpoint = int((start + stop)/2)
    if start > stop:                #COMP
        flag = False
        location = -1
    elif (A[midpoint] == target):   #COMP
        flag = True
        location = midpoint
    elif (target < midpoint):       #COMP
        binarySearch(A,start, midpoint-1, target)
    else:
        binarySearch(A, midpoint+1,stop,target)

    return(flag,midpoint)



#Warning: this function is designed to work with searches that come back with a
#true result, the search functions return [-1] if the item is not found.
def main(A):
    trials = 100
    totalComparisonsLinear = 0
    totalComparisonsBinary = 0
    for i in range(trials):
        randomItem = A[round(random()*len(A))-1]
        totalComparisonsLinear += linearSearch(A,randomItem)[1]
    print("Avg. comparisons (LinearSearch): ", totalComparisonsLinear/trials)

    for i in range(42):
        randomItem = A[round(random()*len(A))-1]
        totalComparisonsBinary += binarySearch(A,0,len(A)/2,randomItem)[1]

    print("Avg. comparisons (LinearSearch): ", totalComparisonsBinary/trials )


A = [1,2,3,4,5,6,7,8,9]
main(A)
