# employee.py
# This file defines the Employee class.

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        # Save the employee's first name
        self.first_name = first_name
        # Save the employee's last name
        self.last_name = last_name
        # Save the employee's annual salary
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """
        Increase the employee's salary.
        - If no amount is given, default raise is $5000.
        - If an amount is given, use that instead.
        """
        self.annual_salary += amount
