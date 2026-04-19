import json

# Ask the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Open a file in write mode and save the number using json.dumps()
with open("favorite_number.json", "w") as f:
    json.dump(favorite_number, f)  # store as JSON

print("Your favorite number has been saved!")

import json

# Open the file in read mode and load the number
with open("favorite_number.json") as f:
    favorite_number = json.load(f)  # read JSON back into Python

# Print the message with the stored number
print(f"I know your favorite number! It’s {favorite_number}.")


import json

def get_favorite_number():
    """Ask the user for their favorite number and save it."""
    favorite_number = input("What is your favorite number? ")
    with open("favorite_number.json", "w") as f:
        json.dump(favorite_number, f)
    return favorite_number

def read_favorite_number():
    """Try to read the favorite number from file."""
    try:
        with open("favorite_number.json") as f:
            return json.load(f)
    except FileNotFoundError:
        # If file doesn’t exist, return None
        return None

def main():
    favorite_number = read_favorite_number()
    if favorite_number:
        print(f"I know your favorite number! It’s {favorite_number}.")
    else:
        favorite_number = get_favorite_number()
        print(f"Got it! I’ll remember your favorite number: {favorite_number}.")

main()

import json

def get_user_info():
    """Ask for multiple pieces of user info and store in a dictionary."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    hobby = input("What is your favorite hobby? ")

    user_info = {
        "username": username,
        "age": age,
        "hobby": hobby
    }

    # Save dictionary to file
    with open("user_info.json", "w") as f:
        json.dump(user_info, f)

    return user_info

def read_user_info():
    """Read user info dictionary back from file."""
    try:
        with open("user_info.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def main():
    user_info = read_user_info()
    if user_info:
        print("Here’s what I remember about you:")
        print(f"Name: {user_info['username']}")
        print(f"Age: {user_info['age']}")
        print(f"Hobby: {user_info['hobby']}")
    else:
        user_info = get_user_info()
        print("Thanks! I’ll remember this info for next time.")

main()

import json

def get_new_username():
    """Ask for a new username and save it."""
    username = input("What is your name? ")
    with open("username.json", "w") as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user, verifying if the stored username is correct."""
    try:
        with open("username.json") as f:
            username = json.load(f)
    except FileNotFoundError:
        username = get_new_username()

    # Verify if this is the correct user
    print(f"Is your username {username}?")
    answer = input("Enter 'y' for yes or 'n' for no: ")

    if answer.lower() == 'y':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"Got it. I’ll remember your username as {username}.")

greet_user()
