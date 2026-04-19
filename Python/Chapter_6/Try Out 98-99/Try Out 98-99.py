# -------------------------------
# 6-1. Person
# -------------------------------

# Create a dictionary (like a mini database) to store information about a person.
# Each piece of information has a "key" (like 'first_name') and a "value" (like 'Samuel').
person = {
    'first_name': 'Samuel',
    'last_name': 'Herbert',
    'age': 28,
    'city': 'Johannesburg'
}

# Print each piece of information from the dictionary.
print("First name:", person['first_name'])
print("Last name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])


# -------------------------------
# 6-2. Favorite Numbers
# -------------------------------

# Create a dictionary where each person’s name is the key
# and their favorite number is the value.
favorite_numbers = {
    'Jaden': 7,
    'Mia': 12,
    'Chris': 3,
    'Sophia': 9,
    'Liam': 21
}

# Loop through the dictionary and print each person’s favorite number.
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")


# -------------------------------
# 6-3. Glossary
# -------------------------------

# Create a dictionary (called glossary) where programming terms are the keys
# and their meanings are the values.
glossary = {
    'variable': 'A name that stores a value in memory.',
    'loop': 'A way to repeat actions multiple times.',
    'function': 'A block of code that performs a specific task.',
    'list': 'A collection of items stored in order.',
    'dictionary': 'A collection of key-value pairs.'
}

# Loop through the glossary and print each word with its meaning.
# Use \n to add a blank line between entries for neat formatting.
for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")
