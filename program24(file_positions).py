"""
File Positions
The tell() method tells you the current position within the file; in other words,
the next read or write will occur at that many bytes from the beginning of the file.
"""
f = open("file2.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
"""
The seek(offset[, from]) method changes the current file position.
The offset argument indicates the number of bytes to be moved.
The from argument specifies the reference position from where the bytes are to be moved
"""
# Open a file
fo = open("file2.txt")
str = fo.read()
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(5)
print ("Again read String is : ", str)
# Close opend file
fo.close()