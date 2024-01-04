def rever_string(string):
    string_list = list(string)

    left = 0
    right = len(string_list)-1

    while left<right:
        if string_list[left].isalnum() and string_list[right].isalnum():
            string_list[left],string_list[right] = string_list[right], string_list[left]

            left +=1
            right -=1


    return ''.join(string_list)

print(rever_string('awanish'))