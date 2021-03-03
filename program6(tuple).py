# tuple(immutable-can't change)
tp = (1, 2, 3)
print("tuple:", tp)

# single tuple
tp1 = (1,)
print("single tuple:", tp1)

# swapping
a = 2
b = 9
a, b = b, a
print("swap:", a, b)

# tuple in tuple(nesting)
tp2 = (("one", 1), 2, 3)
print("tuple in tuple:", tp2)
