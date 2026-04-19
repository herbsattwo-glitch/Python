# test_cities.py

# Import the function from city_functions.py
from city_functions import city_country

# Test 1: City and Country only
def test_city_country():
    """Test that city_country() works with just city and country."""
    result = city_country('santiago', 'chile')
    # The expected result should be 'Santiago, Chile'
    assert result == 'Santiago, Chile'

# Test 2: City, Country, and Population
def test_city_country_population():
    """Test that city_country() works with city, country, and population."""
    result = city_country('santiago', 'chile', 5000000)
    # The expected result should be 'Santiago, Chile - population 5000000'
    assert result == 'Santiago, Chile - population 5000000'
