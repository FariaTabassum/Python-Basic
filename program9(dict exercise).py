#Create a dictonary and take input from the user and return the meanig of the word from the dictonary

print("Enter the word(Set,Append,Mutable,Immutable,String): ")
word = input("Enter Your word: ")
meaning = {"Set" : "Well defined set of objects",
           "Append" :"add (something) to the end of a written document",
           "Mutable": "liable to change",
           "Immutable" : "unchanging over time or unable to be changed",
           "String" : "material consisting of threads of cotton, hemp, or "
                      "other material twisted together to form a thin length"}
print("The meaning of the word: ", meaning[word])

#OR
meanings = {"smother" : "death by suffocting", "morale" : "self decipline, confidence", "vicinity" : "surrounding area", "timid" : "show lack of courage or confidence"}
print("enter words")
inpdic = input()
print("the meaning of the word " + inpdic + " is: " + meanings[inpdic])