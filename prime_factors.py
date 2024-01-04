def prime_factors(num):
    temp = num

    i = 2
    while temp>1:
        if temp%i==0:
            print(i, end = ',')
            temp = int(temp/i)
        else:
            i +=1

prime_factors(12)
        
