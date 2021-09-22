"""
Program: hourly_employee_input.py
Author: Andy Volesky
Last date modified: 09/21/2021

The purpose of this program:

Write a function called hourly_employee_input that asks the user for
a name (string), hours worked (int) and an hourly pay rate (float) and
prints a string including the information.

Include a docstring as your first line declaring what the function does.

Run the script in a shell.

Call the function, entering expected values, numbers in appropriate range
Call the function, entering negative numbers
Call the function, entering bad input (letters, symbols)
What do you need to add to your function for bad input? Handle the bad input
"""


def hourly_employee_input():
    name = str(input('Name? '))
    hours_worked = float(input('Hours worked? '))
    pay_rate = float(input('Pay rate? '))
    print(f'Hello {name}, you worked {hours_worked} hours at ${pay_rate} per hour.')

if __name__ == '__main__':
    hourly_employee_input()

#Call the function, entering expected values, numbers in appropriate range - works OK.
#Call the function, entering negative numbers - No errors, but values make no sense.
#Call the function, entering bad input (letters, symbols) - Get Errors
#What do you need to add to your function for bad input? Handle the bad input - Need to add input validation for each