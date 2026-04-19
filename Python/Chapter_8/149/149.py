# -------------------------------
# 8-12. Sandwiches
# -------------------------------

# Define a function that accepts any number of items for a sandwich.
# The *items parameter means "accept as many arguments as the user provides".
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

# Call the function three times with different numbers of arguments.
make_sandwich('ham', 'cheese')
make_sandwich('turkey', 'lettuce', 'tomato', 'mayo')
make_sandwich('chicken', 'bacon', 'avocado', 'cheddar', 'ranch')


# -------------------------------
# 8-13. User Profile
# -------------------------------

# Define a function that builds a profile using keyword arguments.
# **user_info means "accept any number of key=value pairs".
def build_profile(first_name, last_name, **user_info):
    # Start with a dictionary containing the first and last name.
    profile = {
        'first_name': first_name,
        'last_name': last_name
    }
    # Add all other key-value pairs into the dictionary.
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build a profile of yourself by passing in first/last name and extra info.
my_profile = build_profile(
    'Samuel', 'Herbert',
    occupation='Multimedia Designer',
    location='Johannesburg',
    hobby='Gaming'
)

# Print the dictionary to see the stored information.
print("\nMy Profile:")
print(my_profile)


# -------------------------------
# 8-14. Cars
# -------------------------------

# Define a function that stores car information in a dictionary.
# manufacturer and model are required, but **options allows extra details.
def make_car(manufacturer, model, **options):
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    # Add any extra keyword arguments into the dictionary.
    for key, value in options.items():
        car_info[key] = value
    return car_info

# Call the function with required info and extra details.
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to confirm all info is stored.
print("\nCar Information:")
print(car)
