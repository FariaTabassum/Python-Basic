"""
Exercise#
The task is to create a "Health Management System." Suppose you are a fitness trainer and nutritionist. You have to deal with three clients, i.e., (Harry, Rohan, Hammad). For each client, you have to design their exercise and diet plan.

Instructions:
Create a food log file for each client
Create an exercise log file for each client.
Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name. After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".
Use function
def getdate():
           import datetime
           return datetime.datetime.now()
The purpose of this function is to give time with every record of food or exercise added in the file.
Write a function to retrieve exercise or food file records for any client.
"""
def getdate():
    import datetime
    return datetime.datetime.now()

def choose(k):
    if k == 1:
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("Type here\n")
            with open("afra-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("afra-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("Type here\n")
            with open("nabila-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("nabila-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("Type here\n")
            with open("juhi-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("juhi-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("Please enter valid input (1(Afra),2(Nabila),3(Juhi)")

def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("afra-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("afra-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("nabila-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("nabila-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("juhi-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("juhi-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Plz enter valid input (Afra,Nabila,Juhi)")
print("Health Management System")
a=int(input("Press 1 for log the value and 2 for retrieve "))
if a==1:
    b = int(input("Press 1 for Afra ,2 for Nabila, 3 for Juhi"))
    choose(b)
else:
    b =  int(input("Press 1 for Afra ,2 for Nabila, 3 for Juhi"))
    retrieve(b)







