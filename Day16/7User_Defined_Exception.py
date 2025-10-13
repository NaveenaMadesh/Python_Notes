'''try:
    print(x)
except NameError:
    print("No x is found!!!")
finally:
    print("The try and execpt is finished!!!")'''


# ZeroDivisionError--> those are in built class

'''class checkAgeException(Exception):
    age = int(input("Enter your child age: "))

    if age >= 5:
        print("Eligible for vote!!")

    else:
        raise Exception("Please enter valid age")

n = int(input("Enter a number:"))
if n<0:
    raise Exception("Value shouldn't be negative!!")'''

class Error(Exception):
    pass

class Zerodivision(Error):
    pass

try:
    n = int(input("Enter a number: "))
    if n==0:
        raise Zerodivision
except Error:
    print("You Cannot divide any number by zero..blah!blah!..")
except Zerodivision:
    print("You Cannot divide any number by zero..")
