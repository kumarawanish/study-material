# Complicated dictionary of dictionaries
complicated_dict = {
    'user1': {
        'name': 'John Doe',
        'age': 30,
        'email': 'john@example.com',
        'address': {
            'city': 'New York',
            'zipcode': '10001',
            'country': 'USA'
        },
        'hobbies': ['reading', 'cooking', 'sports']
    },
    'user2': {
        'name': 'Jane Smith',
        'age': 25,
        'email': 'jane@example.com',
        'address': {
            'city': 'San Francisco',
            'zipcode': '94105',
            'country': 'USA'
        },
        'hobbies': ['painting', 'photography', 'traveling']
    }
}

# Accessing data from the complicated dictionary
print(complicated_dict['user1']['name'])  # Output: John Doe
print(complicated_dict['user2']['address']['city'])  # Output: San Francisco
print(complicated_dict['user1']['hobbies'][1])  # Output: cooking
print(complicated_dict.keys())