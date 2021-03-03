"""1)when we use more than one conditions that rely on if then we can take advantage
   of logical operator.
   2)Logical operators are (and,or,not)
"""
# for and operator:all conditions must be true
'''num1 = 90
num2 = 110
num3 = 80
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)'''

# for or operator:
ch = input()
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("vowel")
else:
    print("constant")
