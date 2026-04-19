# test_employee_no_fixture.py
# This file tests the Employee class WITHOUT using a fixture.
# Each test creates its own Employee object.

from employee import Employee  # Import the Employee class

def test_give_default_raise():
    # Step 1: Create an employee with a starting salary of 50,000
    emp = Employee("John", "Doe", 50000)
    # Step 2: Call give_raise() with no arguments (default raise = 5000)
    emp.give_raise()
    # Step 3: Check that the salary is now 55,000
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    # Step 1: Create an employee with a starting salary of 60,000
    emp = Employee("Jane", "Smith", 60000)
    # Step 2: Call give_raise() with a custom raise of 10,000
    emp.give_raise(10000)
    # Step 3: Check that the salary is now 70,000
    assert emp.annual_salary == 70000
