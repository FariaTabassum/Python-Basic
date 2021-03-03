#without global keyword we can't change global variable
l = 10#global
def function1(n):
    l=5#LOCAL
    m=8
    l=l+10
    print("only change local variable",l,m)
function1("without global keyword can't change global variable")
print("Global variable:",l)
#using global keyword we can change global variable
l = 10#global
print("present global variable:", l)
def function1(n):
    #l=5#LOCAL
    m=8
    global l
    l=l+10
    print("add global variable by 10:",l,m)
function1("without global keyword can't change global variable")
print("after Changing Global variable:",l)