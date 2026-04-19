# test_employee_with_fixture.py
# This file tests the Employee class WITH a fixture.
# A fixture creates one Employee object that both tests can reuse.

import pytest
from employee import Employee  # Import the Employee class

# Step 1: Define a fixture that makes an Employee object
@pytest.fixture
def sample_employee():
    # This employee starts with a salary of 40,000
    return Employee("Alice", "Johnson", 40000)

def test_give_default_raise(sample_employee):
    # Step 2: Use the fixture employee
    # Call give_raise() with no arguments (default raise = 5000)
    sample_employee.give_raise()
    # Step 3: Check that the salary is now 45,000
    assert sample_employee.annual_salary == 45000

def test_give_custom_raise(sample_employee):
    # Step 2: Use the fixture employee
    # Call give_raise() with a custom raise of 8,000
    sample_employee.give_raise(8000)
    # Step 3: Check that the salary is now 48,000
    assert sample_employee.annual_salary == 48000
