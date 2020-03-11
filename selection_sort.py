#Coloca o menor elemento do array na primeira posição não correta do array.

def selection_sort(arr):                    #O(n²)
    for pivot in range(len(arr)):
        swaped = False
        for i in range(pivot,len(arr)-1):
            if(arr[pivot]>arr[i+1]):
                swaped = True
                arr[pivot],arr[i+1] = arr[i+1],arr[pivot]
        if(not swaped):
            break
    return arr

l = [6,8,1,4,10,7,8,9,3,2,5]
print(selection_sort(l))