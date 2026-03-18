# Start an infinite loop that keeps asking for toppings
while True:
    # Ask the user for a topping
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    # If the user types 'quit', break out of the loop
    if topping.lower() == 'quit':
        print("Finished adding toppings!")
        break

    # Otherwise, confirm the topping is added
    print(f"I'll add {topping} to your pizza.")



# Start an infinite loop to keep asking for ages
while True:
    # Ask the user for their age
    age_input = input("Enter your age (or 'quit' to stop): ")

    # If they type 'quit', break out of the loop
    if age_input.lower() == 'quit':
        print("Thanks for using the ticket system!")
        break

    # Convert the input into a number
    age = int(age_input)

    # Decide ticket price based on age
    if age < 3:
        print("Your ticket is FREE!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")



# Loop runs until user types 'quit'
topping = ""
while topping != "quit":
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping != "quit":
        print(f"Adding {topping} to your pizza.")



# Use a flag (True/False) to control loop
active = True
while active:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping == "quit":
        active = False  # Turn off the loop
    else:
        print(f"Adding {topping} to your pizza.")


while True:  # Infinite loop
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping == "quit":
        break  # Exit immediately
    print(f"Adding {topping} to your pizza.")


# Infinite loop that never stops
while True:
    print("This loop will run forever!")
