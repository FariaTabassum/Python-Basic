# Dictionary
"""#type
d1 = {}
print(type(d1))

# print dict
d2 = {"A": 1, "B": 2, "C": "D"}
# print("DICT:", d2)
print("DICT:", d2["A"])

# Nesting Dict
d3 = {"A": 1, "B": 2, "C": "D", "E": { "k": 1, "l": 2, "m": "o"}}
print("DICT:", d3["E"])
print("DICT in dct:", d3["E"]["l"])

# Add,delete items
d4 = {"A": 1, "B": 2, "C": 7}
d4["E"] = 5
del d4["B"]
print("DICT:", d4)

# function
d5 = {"A": 0, "B": 7, "C": 7}
# copy()
# print(d5.copy())
d6=d5.copy()
del d5["A"]
print(d6)

# Update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

# key ()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

# values()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#Loop
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x ,y in car.items():
    print(x,y)

print(car.get("brand"))"""

#nested Dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily.get("child1"))
print(myfamily.get("child6","Not a valid Key"))
print(myfamily.get("child3","Not a valid Key"))



