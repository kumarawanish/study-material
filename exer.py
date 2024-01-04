
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

# print(new_l)





#     Given a square matrix mat, return the sum of the matrix diagonals.
# 
#    Only include the sum of all the elements on the primary diagonal and all the #    

#    elements on the secondary diagonal that are not part of the primary diagonal.
#    Input: mat = [[1,2,3],
#              [4,5,6],
#              [7,8,9]]
#    Output: 25
#    Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
#    Notice that element mat[1][1] = 5 is counted only once.

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

diagonal_sum = 0
n = len(matrix)
for i in range(n):
    diagonal_sum +=  matrix[i][i]
    diagonal_sum += matrix[i][n-1-i]


if n % 2 == 1:
    diagonal_sum -= matrix[n // 2][n // 2]

print(diagonal_sum)





