import time
import random as rand

''' test function '''
def assertAscending(arr):
    lastItem = arr[0]
    for items in arr:
        if(items>lastItem):
            return False
    return True
    pass
def mergeSort():
    pass
''' helper function '''
def merge():
    pass
def insertionSort():
    pass
''' driver function '''
def main():
    arrToSort = [rand.randint(1,100) for x in range(1,100)]
    print("array before sort")
    print(arrToSort)

if __name__ == '__main__':
    main()
