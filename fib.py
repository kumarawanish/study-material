def fib(n):
    series = [0, 1]

    for i in range(2, n):
        next_num = series[-1] + series[-2]
        series.append(next_num)

    return series

fib_series = fib(10)
print(fib_series)