"""
Program: multiply_string.py
Author: Andy Volesky
Last date modified: 09/22/2021

The purpose of this program:

write a function multiply_string() that takes a string message and a number n and
returns the string with message printed n times.
"""


"""accepts string and n and returns statement
:param string accepts any string
:param n accepts any integer
:returns copies the string n times and returns
"""
def multiply_string(string, n):
    return n*string


if __name__ == '__main__':
    try:
        spam = multiply_string('Python 1! ', 6)
    except ValueError:
        print("Wrong Input")
    else:
        print(spam)