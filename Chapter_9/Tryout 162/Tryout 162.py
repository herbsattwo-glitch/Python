# Define a class called Restaurant
class Restaurant:
    # The __init__ method runs automatically when you create a new Restaurant object
    def __init__(self, restaurant_name, cuisine_type):
        # Store the restaurant name
        self.restaurant_name = restaurant_name
        # Store the type of cuisine
        self.cuisine_type = cuisine_type

    # Method to describe the restaurant
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    # Method to indicate the restaurant is open
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance (object) of Restaurant
restaurant = Restaurant("Mama’s Kitchen", "Italian")

# Print the attributes individually
print(restaurant.restaurant_name)   # Prints the restaurant name
print(restaurant.cuisine_type)      # Prints the cuisine type

# Call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()



# Create three different Restaurant objects
restaurant1 = Restaurant("Sushi World", "Japanese")
restaurant2 = Restaurant("Taco Fiesta", "Mexican")
restaurant3 = Restaurant("Burger Hub", "American")

# Call describe_restaurant() for each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# Define a class called User
class User:
    def __init__(self, first_name, last_name, age, email, location):
        # Store basic user info
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    # Method to describe the user
    def describe_user(self):
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    # Method to greet the user
    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

# Create several user instances
user1 = User("Alice", "Johnson", 28, "alice@example.com", "New York")
user2 = User("Bob", "Smith", 35, "bob@example.com", "London")
user3 = User("Charlie", "Brown", 22, "charlie@example.com", "Johannesburg")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()



