"""
Program: hourly_employee_input_return.py
Author: Andy Volesky
Last date modified: 09/21/2021

The purpose of this program:

Make a copy of your .py file containing the function called hourly_employee_input
that asks the user for a name (string), hours worked (int) and an hourly pay rate (float)
and prints a string including the information.

Write a function weekly_pay that accepts in the parameter list the hours_worked and hourly_pay_rate
and returns the calculated weekly pay.

Make a function call in hourly_employee_input

Change the string in hourly_employee_input  to print name and weekly pay
Change the hourly_employee_input instead of printing, return a statement and print the result in the main
Include a docstring as your first line declaring what the function does.
"""


def hourly_employee_input():
    name = str(input('Name? '))
    hours_worked = int(input('Hours worked? '))
    pay_rate = float(input('Pay rate? '))
    print(f'Hello {name}, you worked {hours_worked} hours at ${pay_rate} per hour.')

if __name__ == '__main__':
    hourly_employee_input()