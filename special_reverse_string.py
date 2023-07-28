def reverse_string(s):

    string_list = list(s)

    left = 0
    right = len(string_list) - 1

    while left < right:

        if not string_list[left].isalnum():
            left += 1

        elif not string_list[right].isalnum():
            right -= 1

        else:
            string_list[left], string_list[right] = string_list[right], string_list[left]

            left += 1
            right -= 1

    return ''.join(string_list)

print(reverse_string(s = "a,281b$c"))