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


name = str(input('Name? '))
hours_worked = float(input('Hours worked? '))
pay_rate = float(input('Pay rate? '))

"""accepts hours worked and pay rate and calculates total pay
:param hours_worked, total hours worked for the week
:param pay_rate, the $/hr pay rate
:returns the calculation of the total pay
"""
def weekly_pay(hours_worked, pay_rate):
    return hours_worked*pay_rate

"""
calculates total pay and returns a statement
:returns statement 
"""
def hourly_employee_input():
    total = weekly_pay(hours_worked, pay_rate)
    return f'Hello {name}, you made {total}'

if __name__ == '__main__':
    pay_statement = hourly_employee_input()
print(pay_statement)