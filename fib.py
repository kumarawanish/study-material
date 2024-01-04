def fib(n):
    series = [0, 1]

    if n<=0:
        return 'Please enter valid number'

    for i in range(2, n):
        next_num = series[-1] + series[-2]
        series.append(next_num)

    return series

fib_series = fib(0)
# print(fib_series)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
n = 10  # You can change this to compute the Fibonacci number at a different position.
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")