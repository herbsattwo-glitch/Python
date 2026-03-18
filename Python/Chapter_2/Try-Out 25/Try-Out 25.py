# 2-3. Personal Message
# Step 1: Store a person's name in a variable
name = "Eric"

# Step 2: Print a message using that variable
# We use + to join strings together
print("Hello " + name + ", would you like to learn some Python today?")

# 2-4. Name Cases
name = "eric"

# Print the name in lowercase
print(name.lower())   # lower() makes all letters small

# Print the name in uppercase
print(name.upper())   # upper() makes all letters BIG

# Print the name in title case
print(name.title())   # title() capitalizes the first letter of each word

# 2-5. Famous Quote
# Just print the quote directly
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# 2-6. Famous Quote 2
# Store the famous person's name in a variable
famous_person = "Albert Einstein"

# Build the message using concatenation
message = famous_person + ' once said, "A person who never made a mistake never tried anything new."'

# Print the message
print(message)

# 2-7. Stripping Names
# Store a name with extra whitespace (tabs and newlines)
name = "\t\n Eric \n\t"

# Print the original name (with whitespace showing)
print("Original:", name)

# Remove whitespace from the left side only
print("lstrip():", name.lstrip())   # removes spaces/tabs/newlines on the LEFT

# Remove whitespace from the right side only
print("rstrip():", name.rstrip())   # removes spaces/tabs/newlines on the RIGHT

# Remove whitespace from both sides
print("strip():", name.strip())     # removes spaces/tabs/newlines on BOTH sides

# 2-8. File Extensions
# Store a filename in a variable
filename = "python_notes.txt"

# Remove the ".txt" part using removesuffix()
print(filename.removesuffix(".txt"))
