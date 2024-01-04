def solution(lst, target):
    pairs = []
    firstindex = 0
    secondindex = len(lst) - 1

    while firstindex < secondindex:

        if lst[firstindex] + lst[secondindex] == target:
            pairs.append((firstindex, secondindex))
            firstindex += 1
            secondindex -= 1

        elif lst[firstindex] + lst[secondindex] < target:
            firstindex += 1

        else:
            secondindex -= 1

    if not pairs:
        print("No pair found with the given target sum")
    else:
        print("Pairs found with the given target sum:")
        print(pairs)
        # for pair in pairs:
        #     print(f"Index {pair[0]} and Index {pair[1]}")

# Call the function here
solution([1, 2, 3, 4, 5, 6], 5)