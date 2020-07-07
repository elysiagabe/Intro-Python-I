"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import date

# Define a function...let's call it display_calendar
# takes variable args...0 - 2 arguments are valid
# if 0 args are passed in, display the current date's calendar (today's month and year)
# if 1 arg is passed in, assume it is the month and use the current year (i will assume that they are passing in a valid number from 1-12...could later add error handling to check for this)
# if 2 args are passed in, assume they passed in the month and the year (i will also assume the user is passing in correctly formatted data )

# ORIGINAL SOLUTION: 
def show_cal(*args):
    if len(args) > 3: 
          print("Oops! Please pass in the month and year only.")
          sys.exit()

    if len(args) > 1:
        m = int(args[1])
    else: 
        m = date.today().month

    if len(args) > 2:
        y = int(args[2])
    else: 
        y = date.today().year

    print(calendar.month(y, m))

# SECOND SOLUTION: 
# def show_cal(a, m = date.today().month, y = date.today().year):
#     if len() > 3: 
#         print("Oops! Please enter the month and year only.")
#     else:
#         print(calendar.month(int(y), int(m)))

show_cal(*sys.argv)