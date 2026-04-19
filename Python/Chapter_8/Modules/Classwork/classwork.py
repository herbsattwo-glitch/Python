
# This function makes a pizza.
# 'size' is the diameter of the pizza in inches.
# '*toppings' means you can pass in as many toppings as you want.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    # Loop through each topping and print it
    for topping in toppings:
        print(f"- {topping}")


# This function makes a burger.
# 'size' is the diameter of the burger in inches.
# '*ingredients' means you can pass in as many ingredients as you want.
def make_burger(size, *ingredients):
    """Summarize the burger we are about to make."""
    print(f"\nMaking a {size}-inch burger with the following ingredients:")
    # Loop through each ingredient and print it
    for ingredient in ingredients:
        print(f"- {ingredient}")
