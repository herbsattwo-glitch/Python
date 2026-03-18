# Step 1: Create a dictionary called user_info
# A dictionary is like a box with labels (keys) and values inside.
user_info = {
    "first_name": "Herbert",       # The person's first name
    "last_name": "Adogo",         # The person's last name
    "location": "Johannesburg"    # The city where the person lives
}

# Step 2: Build a sentence using f-string formatting
# f-strings let us insert values from the dictionary directly into text.
full_name = f"{user_info['first_name']} {user_info['last_name']} from {user_info['location']}."

# Step 3: Print the sentence to the screen
# print() shows the result in the console.
print(full_name)
