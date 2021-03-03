# Exercise
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
print("Pattern printing")
n=int(input())
print("Enter 1 or 0")
bool_val=input("1 for True value or 0 for False : ")
if bool_val== "1":
    for i in range(0,n + 1):
        print(i * "*")
if bool_val=="0":
    for i in range(n,0,-1):
        print("*"* i)