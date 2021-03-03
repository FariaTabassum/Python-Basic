"""A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
*functions are two types (1) Library -> print(),input() (2) user define"""
#sum of two numbers using functions
# built in function:
a=9
b=8
c= sum ((a,b))
print(c)
# user defined function
def add(a,b):
    sum = a + b
    print(sum)
add(20,40)
# if we store any value into a variable
def function(a,b):
    """ This is a function which will calculate average of Two numbers(docstrings)"""
    average = (a+b)/2
    return  average
v = function(8,9)
print(function.__doc__)
print(v)