'''try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    c=n1/n2
except ZeroDivisionError as msg:
    print(msg)#division by zero # default error message
    print(type(msg))
    print(e.__class__)
    print(e.__class__.__name__)
except ValueError as e:
    print(e)
print("rest of the code!!")


try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    c=n1/n2
except (ZeroDivisionError, ArithmeticError,ValueError) as msg:
    print(msg)#division by zero # default error message
    print(type(msg))
    print(msg.__class__)
    print(msg.__class__.__name__)
print("rest of the code!!")'''



'''1. Python tries to run risky code
2. OH NO! An error happens! 
3. Python creates an ERROR OBJECT (like a package 📦)
4. This package contains:
   - Error type (ValueError, ZeroDivisionError, etc.)
   - Error message ("invalid literal for int()...")
   - Other technical info
5. The 'as' keyword says: "Put that package in this variable!"
6. Now you can open the package and see what's inside!'''