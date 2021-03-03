with open("file2.txt") as f:
    a= f. readlines()
    print(a)
#if we run this program it can't works because we use readlines() before.
f = open("file2.txt")
f.readline()
f.close()