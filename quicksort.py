

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

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quicksort(l))
