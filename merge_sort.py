def merge_sorted(arr1, arr2): # It takes the two sorted array
    i = j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i]) 

            i += 1

        else:
            merged.append(arr2[j])

            j += 1

    while i< len(arr1):
        merged.append(arr1[i])
        i +=1

    while j< len(arr2):
        merged.append(arr2[j])
        j +=1
            
    return merged




def merge_sort(arr): # It divides the array in multiple parts according to the requirements to make the sorted array
    
    if len(arr) ==1:
        return arr
    
    mid = (len(arr))//2

    left = arr[ :mid]
    right = arr[mid: ]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted(left, right)

print(merge_sort([6,9,11,2,4]))


    
    
    



 

