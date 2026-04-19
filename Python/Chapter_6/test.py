# We are creating a dictionary called 'users'
# A dictionary in Python stores data in key-value pairs
users = {
    'L' : {   # 'L' is the username (the key)
        'name' : 'B',     # Inside 'L', we store another dictionary with details
        'surname' : 'R',
        'age' : 12
    },
    'A' : {   # 'A' is another username (the key)
        'name' : 'N',
        'surname' : 'P',
        'age' : 15
    }
}

# Loop through each item in the 'users' dictionary
# 'username' will be the key ('L' or 'A')
# 'user_info' will be the inner dictionary with name, surname, and age
for username, user_info in users.items():
    # Print the username and the whole inner dictionary
    print(f"\nUsername: {username} {user_info}")
    
    # Access values from the inner dictionary
    # Get the 'name' and 'surname' and join them together into one string
    full_name = f"{user_info['name']} {user_info['surname']}"
    
    # Get the 'age' value from the inner dictionary
    age = user_info['age']
    
    # Print the full name
    print(f"Full Name: {full_name}")
    
    # Print the age
    print(f"Age: {age}")
