# -------------------------------
# 5-8. Hello Admin
# -------------------------------

# Make a list of usernames. One of them must be 'admin'.
usernames = ['admin', 'Jaden', 'Mia', 'Chris', 'Sophia', 'Liam']

# Loop through each username in the list
for user in usernames:
    # If the username is 'admin', print a special message
    if user.lower() == 'admin':
        print("Hello admin, would you like to see a status report?")
    # Otherwise, print a normal greeting
    else:
        print(f"Hello {user}, thank you for logging in again.")


# -------------------------------
# 5-9. No Users
# -------------------------------

# Start with an empty list of usernames
usernames = []

# Check if the list has any users
if usernames:
    # If the list is NOT empty, greet each user
    for user in usernames:
        if user.lower() == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    # If the list IS empty, print this message
    print("We need to find some users!")


# -------------------------------
# 5-10. Checking Usernames
# -------------------------------

# Current usernames already taken
current_users = ['admin', 'Jaden', 'Mia', 'Chris', 'Sophia']

# New usernames people want to use
new_users = ['mia', 'Liam', 'john', 'Admin', 'Ella']

# Make a lowercase copy of current_users so we can compare without worrying about capital letters
current_users_lower = [user.lower() for user in current_users]

# Check each new username
for new_user in new_users:
    # If the lowercase version of the new username is already in the list, it’s taken
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new one.")
    else:
        # Otherwise, it’s available
        print(f"The username '{new_user}' is available.")


# -------------------------------
# 5-11. Ordinal Numbers
# -------------------------------

# Make a list of numbers from 1 to 9
numbers = list(range(1, 10))

# Loop through each number
for number in numbers:
    # Special endings for 1, 2, and 3
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        # All other numbers just get 'th'
        print(f"{number}th")
