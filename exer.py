
def new():

    l = [1,2,3,4,6,9,7]

    print(l)

    left = 0
    right = len(l)-1

    result = []
    while left<=right:
        if left == right:
            result.append(l[left])
            return result
        result.append(l[left] + l[right]) 
        left += 1
        right -= 1

# print(new())

l = [1,2,3,4,6,9,7,9,6]
new_l = []

for i in range(len(l)):
    if i == (len(l)//2):
        if (len(l)) %2 == 0:
            break
        else:
            new_l.append(l[(len(l)//2)])
            break
    new_l.append(l[i]+l[-(i+1)])

print(new_l)




