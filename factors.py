def fac(numbers):

    factors_list = {}

    for number in range(1, numbers+1):
        
        factor_list = []

        for i in range(1,number+1):
            if number%i==0:
                factor_list.append(i)

        # factors_list[number] = factor_list

    return factors_list


print(fac(10))