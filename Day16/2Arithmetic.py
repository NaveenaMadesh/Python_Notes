try:
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    n3 = n1+n2
    n3 = n1/n2
    print(n3)

except ArithmeticError:
    print("arithmetic error")
#Here If I give n1/0 it means an arithemetic error 
#because arithmetic error is parent class for zero division error
#so it shows as arithmetic error
except ZeroDivisionError:
    print("Cannot Divide by Zero")
    print(n1/2)

#to specific put the zerodivision error at first!!!!
#among general put the specific at first
except ValueError:
     print("Value is not correct")

except:
    print("Enter proper code!!!!")
