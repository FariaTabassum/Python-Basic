'''for loop'''
print('for loop')
print("-------------------")
# List type
print("list")
list=["mango","Banana","Pine","Lotus"]

for item in list:
    print(item)
# list of list
print("\nlist of list")
list = [["mango",30],["Banana",70],["Pine",90],["Lotus",80]]

# for item in list:
    # print(item)
# for item, quantity in list:
    # print(item, quantity)
for item, quantity in list:
    print(item,": quantity =", quantity)

#Dictonary
print("\n Dictonary")
list = [["mango",30],["Banana",70],["Pine",90],["Lotus",80]]
dict1 = dict(list)
print(dict1)
for item, quantity in dict1.items():
    print(item,": quantity =", quantity)

#quiz
'''create  a list and ptint if there was any number which value is greater than six'''
print("\n Quiz")
list1 = ["name",4 ,"call",7 , 10, 60, 9]

for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)
#sum of numbers
print("\nsum of numbers:")
num = [10,80,38,25,76]
sum =0
for x in num:
    sum = sum + x
print(sum)

''' while loop'''
print('\nwhile loop')
print("-------------------")
i= 1
while (i<=20):
    print(i)
    i=i+1
#sum of numbers
print("\nsum of numbers:")
num = [10,80,38,25,76]
i=0
n= len(num)
while (i>n):
        sum= sum + i
        i = i+1
print(sum)