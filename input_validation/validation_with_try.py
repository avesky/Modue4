"""
Program: validation_with_try.py
Author: Andy Volesky
Last date modified: 09/21/2021

The purpose of this program:

You can now update your average test scores code from a previous assignment with added input
validation using try/except.

Details:
Update your previous assignment code to include try/except for each of the user inputs.

If the user enters negative numbers or a string for their number inputs,
the except path should print an error message.
"""

from constants import NUM_SCORES

#asking for Name inputs
try:
    first_name = input('First Name? ')
except:
    print("An Error Occured")
try:
    last_name = input('Last Name? ')
except:
    print("An Error Occured")

#prompting user what is happening
print(f'Hello {first_name} {last_name} you will enter {NUM_SCORES} scores and I will calculate the average for you.')

#asking for Score Inputs
try:
    score1 = int(input('Enter score 1: '))
    score2 = int(input('Enter score 2: '))
    score3 = int(input('Enter score 3: '))
    if (score1 or score2 or score3) < 0:
        raise ValueError("No negative numbers please.")
except:
    print("An Error Occured")
else:
#completing average calculation
    avg = (score1 + score2 + score3 )/NUM_SCORES

#printing result
    print(f'{first_name} {last_name} Your average score is {avg}. Congrats or Condolences as appropriate.')

#tested with 100, 50, and 0 got 50.0 as a result
#tested with 20, 10, and 5 got 11.6666666667 as a result
#testeed with -500, 9000000000, and 0 got 2999999833.3333335 as a result
#tested by entering letters in the scores section - got error due to not being able to conver to an int.
