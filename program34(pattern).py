#pattern
"""
n=3
*
**
***
"""
n=3
for i in range(n+1):
    print(i*"*")
"""
n=4
*
***
*****
*******
"""
n=4
for i in range(n+1):
    print((2*i-1)*"*")