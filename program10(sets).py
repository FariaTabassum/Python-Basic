#Sets: Unordered collection of items
#type
'''s= set()
print(type(s))'''
#rules 1
'''set_from_list = {1, 2, 3, 4, 5}
print("set:", set_from_list)'''
#or
'''list = {1, 2, 3, 4, 5}
set_from_list = (list)
print("set:", set_from_list)'''
#rules 2
'''num = set([1, 2, 3])
print(num)'''

# add ,remove value
'''num = set([1, 2, 3])
num.add(8)
num.remove(8)
print(num)
print(8 in num)'''
# union,intersection,difference
'''num1 = {1, 2, 3, 4, 5}
num2 = set([1, 2, 3])

print("union :", num1 | num2)
print("intersection :", num1 & num2)
print("difference :", num1 - num2)'''
# or
'''num1 = {1, 2, 3, 4, 5}
num = num1.intersection({3,5,2})
num2 = num1.union({3,5,2})
num3 = num1.difference({3,5,2})
print("intersection :",num)
print("union  :",num2)
print("difference  :",num3)'''
# disjoint
'''num={1,2,3,4}
num1 ={5,6}
print(num.isdisjoint(num1))'''






