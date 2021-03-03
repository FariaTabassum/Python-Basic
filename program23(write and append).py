#Write and append mode
'''#f = open("file2.txt","w")
f = open("file2.txt","a")
a = f.write("hello\n")
print(a)
f.close()'''
# handle read or write both
f= open("file2.txt","r+")
print(f.read())
f.write("Hi")

f.close()