"""
Python provides many built-in functions that are predefined and can be used by the programmers by just calling them.
These functions not only ease our work but also create a standard coding environment.
In this tutorial, we will learn about three important functions:
map(), filter, and reduce() in Python. These functions are most commonly used with Lambda function.
 "Lambda functions are functions that do have any name".
"""
#--------------------------MAP------------------------------
#without map
numbers=["3","45","34","30"]
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
numbers[2]=numbers[2]+1
print(numbers[2])
#using map
"""
map(function, iterable) 
A map function takes two parameters:
First one is the function through which we want to pass the items/values of the iterable
The second one is the iterable itself
"""
numbers=["3","45","34","30"]
numbers=list(map(int,numbers))
numbers[2]=numbers[2]+1
print(numbers[2])
#Example
def sq(a):
      return a*a

num = [2,3,5,6,76,3,3,2]
square = list(map(sq, num))
print(square)
#using lambda
num = [2,3,5,6,76,3,3,2]
square = list(map(lambda x: x*x, num))
print(square)
#Example
def square(a):
     return a*a

def cube(a):
    return a*a*a

func = [square, cube]
num = [2,3,5,6,76,3,3,2]
for i in range(5):
      val = list(map(lambda x:x(i), func))
      print(val)

# --------------------------FILTER------------------------------
"""
filter(function, iterable)
It also takes two parameters:
First one is the function for which the condition should satisfy
The second one is the iterable
"""
list_1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)
#--------------------------REDUCE------------------------------
"""
"Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".
Unlike the previous two functions (Filter and Map), we have to import the reduce function from functools module using the statement:
from functools import reduce
We can also import the whole functools module by simply writing
Import functools
But in the case of bigger projects, it is not good practice to import a whole module because of time restraint.
SYNTAX:
reduce(function, iterable)
"""
#without reduce()
list1 = [1,2,3,4,2]
num = 0
for i in list1:
    num = num + i
print(num)
#with reduce()
from functools import reduce
num = reduce(lambda x,y:x*y, list1)
print(num)