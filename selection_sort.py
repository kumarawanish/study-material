def selection_sort(arr):
    min = 0

    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        arr[i], arr[min] = arr[min], arr[i]

    return arr

print(selection_sort([8,7,1,2,9]))


