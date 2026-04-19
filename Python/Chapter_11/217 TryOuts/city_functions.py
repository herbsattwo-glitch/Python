# city_functions.py

# This file contains ONLY the function definition.
# It does not run anything by itself.

def city_country(city, country, population=None):
    """
    Return a string in the format 'City, Country'
    or 'City, Country - population xxx' if population is provided.
    """

    # If population is given, include it in the string
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        # Otherwise, just return City, Country
        return f"{city.title()}, {country.title()}"
