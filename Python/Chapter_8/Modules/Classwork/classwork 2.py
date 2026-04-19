
# Import the functions we created in food_functions.py
# This allows us to use make_pizza and make_burger here.
from classwork import make_pizza, make_burger

# Call the pizza function with a size and toppings.
# The first argument (12) is the size in inches.
# The rest ("pepperoni", "mushrooms", "green peppers") are toppings.
make_pizza(12, "pepperoni", "mushrooms", "green peppers")

# Call the burger function with a size and ingredients.
# The first argument (6) is the size in inches.
# The rest ("beef patty", "cheddar cheese", "lettuce", "tomato", "onions") are ingredients.
make_burger(6, "beef patty", "cheddar cheese", "lettuce", "tomato", "onions")
