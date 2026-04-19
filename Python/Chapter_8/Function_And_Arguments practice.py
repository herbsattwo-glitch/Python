# This creates a function named "drink"
# A function is a block of code that runs when we call it
# It has two inputs (parameters): drink_type and size
# If we do NOT give values, Python will use the default ones
def drink(drink_type='coffee', size='medium'):

    # This line prints the message
    # The f before the string lets us insert variables inside {}
    print(f"\nPreparing a {size} cup of {drink_type}.")

# This calls the function with NO values
# So Python uses the defaults: coffee and medium
drink()

# This calls the function and gives NEW values
# So it replaces the default values
drink(drink_type='tea', size='large')

# Here we still give values, but we switch the order
# Because we wrote the parameter names, Python still understands
drink(size='small', drink_type='hot chocolate')