import time
import random as rand

''' @Author Kaleb Bickmore
    Simple program to test different sorts inside python'''

''' test function '''
def assertAscending(arr):
    lastItem = arr[0]
    for items in arr:
        if(items<lastItem):
            return False
        lastItem=items
    return True
    pass
def mergeSort(arr):
    if(arr==[] or len(arr)==1):
        return arr

    mid = round(len(arr)/2)
    leftSide = mergeSort(arr[0:mid])
    rightSide = mergeSort(arr[mid:len(arr)])
    return merge(leftSide,rightSide)
    pass
''' helper function '''
def merge(leftSide,rightSide):
    sortedMergedArr = []
    while((leftSide!= None and leftSide!= []) or (rightSide!=None and rightSide!= []) ):
        if(leftSide== None or leftSide==[] ):
            sortedMergedArr.append(rightSide.pop(0))
        elif(rightSide == None or rightSide== [] ):
            sortedMergedArr.append(leftSide.pop(0))
        else:
            if(leftSide[0]<rightSide[0]):
                sortedMergedArr.append(leftSide.pop(0))
            else:
                sortedMergedArr.append(rightSide.pop(0))
    return sortedMergedArr
    pass
def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if(arr[j]>arr[j+1]):
                arr[j+1],arr[j] = arr[j],arr[j+1]
    pass
def quickSort(arr,partition):
    if(len(arr)==1 or arr==[]):
        return arr;
    myNum = arr.pop(partition)
    leftArr = [ arr[x] for x in range(len(arr)) if(arr[x]<myNum )]
    rightArr = [ arr[x] for x in range(len(arr)) if(arr[x]>=myNum )]
    sortedLeft = quickSort(leftArr,round(len(leftArr)/2))
    sortedRight = quickSort(rightArr,round(len(rightArr)/2))
    return sortedLeft+[myNum]+sortedRight

    pass
''' driver function '''
def main():
    times = []
    arrToSort = [rand.randint(1,10000) for x in range(1,10000)]
    insertionSortArray = arrToSort[:]
    startTime = time.time()
    insertionSort(insertionSortArray)
    endTime = time.time()
    timeTook = (endTime- startTime)
    times.append(timeTook)
    print("time to sort for insertions sort: "+str(timeTook) +" seconds." )

    if(assertAscending(insertionSortArray)):
        print("insertion sort sorted the array.")
        #print(insertionSortArray)
    else:
        print("insertions sort did not work...")
    mergeSortArray = arrToSort[:]
    startTime = time.time()
    mergeSortArray= mergeSort(mergeSortArray)
    endTime = time.time()
    timeTook = (endTime- startTime)
    times.append(timeTook)
    print("time to sort for merge sort: "+str(timeTook) +" seconds." )
    if(assertAscending(mergeSortArray)):
        print("merge sort sorted the array.")
        #print(mergeSortArray)
    else:
        print("mergeSort did not work...")
    quickSortArray = arrToSort[:]
    startTime = time.time()
    quickSortArray = quickSort(quickSortArray,round(len(quickSortArray)/2))
    endTime = time.time()
    timeTook = (endTime- startTime)
    times.append(timeTook)
    print("time to sort for quick sort: "+str(timeTook) +" seconds." )
    if(assertAscending(quickSortArray)):
        print("quickSort sorted The array")
        #print(quickSortArray)
    else:
        print("quickSort did not work...")
    ''' Crown the fastest sorting algorithm'''
    if(times.index(min(times))==0):
        print("insertionSort probably cheated...")

    if(times.index(min(times))==1):
        print("mergeSort is the winner, time: "+str(min(times)))
    if(times.index(min(times))==2):
        print("quicksort is the winner, time: "+str(min(times)))

if __name__ == '__main__':
    main()
