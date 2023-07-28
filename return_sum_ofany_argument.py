def sum_arguments(*args):
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum

# Example usage:
result = sum_arguments(1, 2, 3, 4, 5)
print(result)  # Output: 15

result = sum_arguments(10, 20, 30)
print(result)  # Output: 60
