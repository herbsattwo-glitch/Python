# Function to make a shirt
def make_shirt(size, message):
    # Print a summary sentence about the shirt
    print(f"The shirt size is {size} and it will say: '{message}'.")

# Call the function using positional arguments
make_shirt("Medium", "Keep Calm and Code On")

# Call the function using keyword arguments
make_shirt(size="Large", message="Python Rocks!")


# Modified function with default values
def make_shirt(size="Large", message="I love Python"):
    # Print a summary sentence about the shirt
    print(f"The shirt size is {size} and it will say: '{message}'.")

# Make a large shirt with default message
make_shirt()

# Make a medium shirt with default message
make_shirt(size="Medium")

# Make a shirt of any size with a different message
make_shirt(size="Small", message="Gaming is Life")



# Function to describe a city
def describe_city(city, country="South Africa"):
    # Print a simple sentence about the city and country
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Johannesburg")          # Uses default country
describe_city("Cape Town")             # Uses default country
describe_city("Reykjavik", "Iceland")  # Overrides default country
