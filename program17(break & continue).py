#break
'''i = 1
while i <= 100 :
    if i ==20 :
        break
    print(i)
    i = i+ 1
print("Hello")

# continue
i = 1
while i <= 100 :
    if i ==20 :
        continue
    print(i)
    i = i+ 1
print("Hello")


# break & continue
i= 0
while (True):
    if i+1<5:
        i = i + 1
        continue
    print(i+1)
    if (i == 44):
        break
    i = i+1'''
#quiz
while (True) :
    inp = int(input ("Enter a number \n"))
    if inp>100:
        print("congrats you have entered a number greater than 100 \n")
        break
    else:
        print("Try again! \n")
        continue
