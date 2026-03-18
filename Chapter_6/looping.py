# Person dictionary
person = {
    'name': 'Alice',
    'age': 30,
}

# Looping through all key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Looping through all keys
for key in person.keys():
    print(key)
################################################################################
# Favorite Colors dictionary
favorite_colors = {
    'Bob': 'blue',
    'Alice': 'green',
    'Charlie': 'red',
}

# Looping through keys in a particular order (alphabetically)
for name in sorted(favorite_colors.keys()):
    print(name)

# Looping through all values in the dictionary
for color in favorite_colors.values():
    print(color)

    