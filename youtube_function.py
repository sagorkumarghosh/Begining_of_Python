#Example:1

"""Function allow us to reuse the code without repeating ourselves. Allow us to put code to specific
purpose to a single location. So updated in one spot will change the function value we dont need to 
change it manually in the code line. This is called dry means not using the same code repetedly. 

def hello_func():
    print("Hello Function!")
hello_func()
hello_func()
hello_func()
hello_func()"""


# Example 2:
"""Function can return the value when operate with code.For example if we want to return some value
from function we need to print out the function

def hello_func():
    return 'Hello Function'

print(hello_func())"""

# Example 3:
""" We can treat the funcion as the data type is return

def hello_func():
    return 'Hello Function'

print(hello_func().upper())"""

# Example 4:
"""Now we need to pass the argument inside our function parenthesis. we will see the positional
argument takes the default value. without using default value we can pass the positional
argument without the default value by passing the value of positional argument when we call 
the function

def hello_func(greeting,name ='man'):
    return "{}, {}".format(greeting,name)

print(hello_func("Hi", name = 'sagor'))"""

# Example 5:

#y = int(input("Enter a Year"))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]
def year(y):
    return y % 4 == 0
    #print("{}, is leap year".format(y))
    #else:
     # print("{}, is not leap year".format(y))

def days_in_month(y, month):
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and year(y):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))