def insertion_sort(arr):            #O(n²)
    for i in range(1,len(arr)):
        pivot = i
        while(arr[pivot]<arr[pivot-1] and pivot>0):
            arr[pivot],arr[pivot-1] = arr[pivot-1],arr[pivot]
            pivot -= 1
    return arr

l = [6,8,1,4,10,7,8,9,3,2,5]
print(insertion_sort(l))