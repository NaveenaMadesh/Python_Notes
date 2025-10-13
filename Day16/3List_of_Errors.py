try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    c =  n1/n2

except(ZeroDivisionError,ValueError,TypeError):
    print("enter valid input")

    