
# error occur that's why can not print 2nd line
"""print("Enter num1:")
num1=input()
print("Enter num2:")
num2 = input()
print("sum",int(num1)+int(num2))
print("This is an important line23")"""
print("Enter num1:")
num1=input()
print("Enter num2:")
num2 = input()
try:
    print("sum",int(num1)+int(num2))
except Exception as e:
    print(e)
print("This is an important line23")