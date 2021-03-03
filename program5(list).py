#List of string
subjects = ["c","c++","java","python","OS"]
print(subjects)
#List index
print(subjects[0])
print(subjects[2])

#operator(in,not in,
#if present in list then return true
print("python" in subjects)
print("Toc" not in subjects)
#if not present in list then return false
print("Toc" in subjects)
#Add list item
print("new items added:",subjects + ["Toc",45])

#copy functions
subjects1=subjects.copy()
print("copied list:",subjects)

#item position
pos= subjects.index("java")
print("Index position:",pos)

#count functions
pos= subjects.count("java")
print("count:",pos)

#clear functions
subjects.clear()
print("cleared all items from list:",subjects)




'''#List of numbers
numbers=[2,3,4,5,8,1]
#List slicing
print(numbers)
print(numbers[2])
print(numbers[0:6])
print(numbers[0:])
print(numbers[:6])
print(numbers[:])
print(numbers[1:4])
print(numbers[ : :1])#by default 1
print(numbers[ : : 2])
print(numbers[ : : 3])
print(numbers[1:5:2])


#List functions
#sort
numbers.sort()
print("sorted list:",numbers)
#reverse
numbers.reverse()
print("reverse list:",numbers)
#length,max,min
print(len("length:",numbers))
print(max("maximum:",numbers))
print(min("minimum:",numbers))

#Append funcrions(add items in end)
numbers.append(9)
print("append:",numbers)

#define empty list and items added by using append functions
num=[]
num.append(9)
num.append(10)
num.append(11)
print("append empty list:",num)

#insert functions
numbers.insert(2,56)#1st argument is a index num,2nd one is value.
print("insert:",numbers)

#remove functions
numbers.remove(56)
print("remove:",numbers)

#pop(last one has been removed)
numbers.pop()
print("pop:",numbers)'''






