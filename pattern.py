# for i in range(1,28):
#     for j in range(1,28):
#         if i>j:
#             print(chr(64+j), end="")
#         else:
#             print(" ", end="")
#     print()

for i in range(1,28):
    for j in range(1,28):
        if i<j:
            print(chr(64+j), end="")
        else:
            print(" ", end="")
    print()