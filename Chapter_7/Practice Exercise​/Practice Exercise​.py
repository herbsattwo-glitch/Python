# Start by setting a flag to control the loop
# True means "keep looping", False means "stop"
keep_running = True

# Use a while loop that runs as long as keep_running is True
while keep_running:
    # Ask the user to enter a number between 1 and 10 or type "quit"
    user_input = input("Enter a number between 1 and 10 (or type 'quit' to exit): ")

    # Check if the user typed "quit"
    if user_input.lower() == "quit":
        # If yes, set the flag to False to stop the loop
        keep_running = False
        # Use break to exit the loop immediately
        break

    # Check if the input is a number (only digits, no letters or symbols)
    if user_input.isdigit():
        # Convert the input string into an integer
        number = int(user_input)

        # Check if the number is within the valid range (1 to 10)
        if 1 <= number <= 10:
            # If the number is 5, exit the loop
            if number == 5:
                print("You entered 5, exiting the loop")
                # Set flag to False and break out of the loop
                keep_running = False
                break
            else:
                # If the number is valid but not 5, just print it
                print(f"You entered: {number}")
        else:
            # If the number is outside 1–10, skip this iteration
            print("Invalid number! Please enter between 1 and 10.")
            continue
    else:
        # If the input is not a number and not "quit", skip this iteration
        print("Invalid input! Please enter a number or 'quit'.")
        continue

# When the loop ends, print a goodbye message
print("Program ended.")
