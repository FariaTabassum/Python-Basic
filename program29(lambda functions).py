#without lambda
def add(a,b):
    return (a+b)
print(add(4,5))
# Lambda functions or anonymous functions
# Not powerful as Named functions
# It can work with single line of code
#using lambda
add = lambda a,b:a+b
print(add(5,9))
#sorting without lambda
def index(a):
    return a[1]
a=[[3,5],[5,1],[9,0],[1,3]]
a.sort(key =index)
print(a)
#sorting using lambda
a =[[1, 14], [5, 6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)