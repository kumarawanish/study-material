def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not present in the list

# Example usage:
if __name__ == "__main__":
    my_list = [4, 2, 6, 8, 3, 1, 9, 5, 7]
    target_value = 3

    result = linear_search(my_list, target_value)
    if result != -1:
        print(f"Target found at index {result}.")
    else:
        print("Target not found in the list.")
