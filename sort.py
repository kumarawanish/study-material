l = [2, 8, 3, 6, 7]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

# print(l)


data_list = [{
    "name": "rahul",
    "age": 20,
    "address": "Mohanjodaro"
},
    {
        "name": "pranjal",
        "age": 14,
        "address": "Denmark"
},
    {
        "name": "rohilla",
        "age": 9,
        "address": "Delhi"
},
]


for i in range(len(data_list)):
    for j in range(i+1, len(data_list)):
        if data_list[i].get("age") > data_list[j].get("age"):
            data_list[i], data_list[j] = data_list[j], data_list[i]


print(data_list)

               