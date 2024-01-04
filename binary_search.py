def binary_search(lst, target):
    low = 0
    high = len(lst)-1
    
    mid_value = (low+high)//2
    
    while low<=high:
        if lst[mid_value] == target:
            return mid_value
        
        elif lst[mid_value] < target:
            mid_value += 1

        elif lst[mid_value] > target:
            mid_value -= 1
            
# lst = [1,2,3,4,5,6]            
# print(binary_search(lst,6))

# Binary search using recursion

def binary_search_recursion(arr, low, high, item):
    if low <= high:
        #search
        mid = (low + high)//2

        if arr[mid] == item:
            return mid
        
        elif arr[mid] > item:
            return binary_search_recursion(arr, low, mid-1, item)
        
        elif arr[mid] < item:
            return binary_search_recursion(arr, mid+1, high, item)

        

    else:
        return -1


print(binary_search_recursion([9,10,11,1,5,6], low = 0, high= len([9,10,11,1,5,6])-1,item=11))


