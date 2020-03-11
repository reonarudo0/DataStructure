def binary_search_iter(arr,n):
    start = 0
    end = len(arr)-1

    while(start<=end or end>=start):
        mid = (start+end)//2
        if(arr[mid] == n):
            while(mid > 0 and arr[mid-1] == n):
                mid = mid - 1
            return ('{} found at {}'.format(n,mid+1))
        elif(arr[mid]<n):
            start = mid+1
        else:
            end = mid-1
    return ('{} not found'.format(n))

n = 9
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search_iter(sorted_arr,n))