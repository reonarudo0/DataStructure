#Coloca o maior elemento na ultima posição não correta do array a cada interação.

def bubble_sort(arr):                   #O(n²)
    for j in range(len(arr)):
        swaped = False
        for i in range(len(arr)-1-j):   #Para cada interação do bubble sort o ultimo elemento fica no lugar correto
            if(arr[i]>arr[i+1]):        #Não tem a nescessidade de ficar recomparando.
                swaped = True
                arr[i], arr[i+1] = arr[i+1],arr[i]
        if (not swaped):                #Se não ocorreu troca, o array está ordenado.
            break
    return arr

l = [6,8,1,4,10,7,8,9,3,2,5]
print(bubble_sort(l))