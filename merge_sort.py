#No merge sort dividimos a lista até sobrar um elemento e depois começamos a comparar e juntar

def merge_sort(arr):                        #O(nlog(n))
    pivot = int(len(arr)/2)                 #Divimos a lista em 2
    left = arr[:pivot]
    right = arr[pivot:]

    if(len(left)>1):                        #Continuamos a dividir até que a lista tenha somente 1 elemento
        left = merge_sort(left)
    if(len(right)>1):
        right = merge_sort(right)

    sorted_arr = []
    while(len(left)>0 and len(right)>0):    #Começamos a juntar, comparando qual o menor elemento em cada lista
        if(left[0] < right[0]):
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    if(len(left)==0):                       #Caso alguma das listas acabe todos os outros elementos da outra lista
        sorted_arr.extend(right)            #são maiores, por isso podemos simplesmente junta-los ao final da lista
    else:
        sorted_arr.extend(left)

    return sorted_arr


l = [6,8,1,4,10,7,8,9,3,2,5]
print(merge_sort(l))