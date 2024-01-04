def find_frequency(lst):
    frequency_dict = {}
    
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    return frequency_dict

# Example usage:
my_list = [1, 2, 3, 1, 2, 1, 4, 3, 2, 5]
result = find_frequency(my_list)
print(result)



#Alternative

from collections import Counter

def find_frequency_using_counter(lst):
    return Counter(lst)

# Example usage:
my_list = [1, 2, 3, 1, 2, 1, 4, 3, 2, 5]
# result = find_frequency_using_counter(my_list)
# print(result)

# my_list.extend(("hello","rahul"))
# print(my_list)