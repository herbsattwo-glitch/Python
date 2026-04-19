# This program asks the user for their name
# Then it saves that name into a file called guest.txt

# Prompt the user to type their name
name = input("Please enter your name: ")

# Open the file 'guest.txt' in write mode ('w')
# If the file doesn't exist, Python will create it
# If the file already exists, it will overwrite the old content
with open("guest.txt", "w") as file:
    # Write the user's name into the file
    file.write(name)

# Let the user know their name was saved
print("Your name has been saved to guest.txt")



# This program keeps asking users for their names
# It saves ALL names into a file called guest_book.txt
# Each name is written on a new line

# Open the file 'guest_book.txt' in write mode ('w')
# Using 'w' will clear the file first, so we start fresh
with open("guest_book.txt", "w") as file:
    while True:
        # Ask the user for their name
        name = input("Please enter your name (or type 'quit' to stop): ")

        # If the user types 'quit', break out of the loop
        if name.lower() == "quit":
            print("Guest book entry complete. All names saved.")
            break

        # Write the name into the file, followed by a newline character
        file.write(name + "\n")

        # Confirm to the user that their name was added
        print(f"{name} has been added to guest_book.txt")
