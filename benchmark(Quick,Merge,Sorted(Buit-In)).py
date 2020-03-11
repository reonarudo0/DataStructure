import time
import random

def quicksort(arr):
    pivot = arr[0]
    left = []
    right = []
    middle = []
    for element in arr:
        if(element < pivot):
            left.append(element)
        elif(element > pivot):
            right.append(element)
        else:
            middle.append(element)

    if(len(left)>1):
        left = quicksort(left)
    if(len(right)>1):
        right = quicksort(right)

    return left + middle + right

def merge_sort(arr):
    pivot = int(len(arr)/2)
    left = arr[:pivot]
    right = arr[pivot:]

    if(len(left)>1):
        left = merge_sort(left)
    if(len(right)>1):
        right = merge_sort(right)

    sorted_arr = []
    while(len(left)>0 and len(right)>0):
        if(left[0] < right[0]):
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    if(len(left)==0):
        sorted_arr.extend(right)
    else:
        sorted_arr.extend(left)

    return sorted_arr

def generateRandomList(size):
    return [random.randint(1, 1000) for i in range(size)]

def analyze_function(function,arr,name):
    t0 = time.time()
    function(arr)
    finalTime = time.time() - t0
    print('{}\t ----> {:1.6f}'.format(name, finalTime))


n=1000
while(n<1000000):
    arr = generateRandomList(n)

    print('Array Size: {}'.format(n))
    analyze_function(quicksort,arr.copy(),'Quicksort')
    analyze_function(merge_sort, arr.copy(),'Merge Sort')
    analyze_function(sorted,arr.copy(),'Built-In')          #equals to array.sort()
    n = n*10
    print('-'*30)


