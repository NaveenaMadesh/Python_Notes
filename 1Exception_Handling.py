#Exception Handling
#Error--> Human mistakes (syntax errors,logical error)
#Done during development

#Syntax error 
#If we violate any rules for syntax then those are syntax error

#Exception
#No error in the code
#Runtime errors 
#unexpected input 



try:
    n1=int(input("Enter a number: "))
    n2= int(input("Enter a number: "))
    c=n1/n2
    print(c)
    
except(ZeroDivisionError):
    print("You cant enter any number by zero!!!!")
    s=n1/2 
    print(s)
except(ValueError):
    print("Please Enter numeric value!!!")
except:#general handling #general except block must be at last
    print("Please enter valid input!!!")



# n1/0 --> we cant divide a number using 0

# Exception handling --> handling the possible error that throws during run time
#responding to the exception
#after exception the program should be in flow

#we can handle that using
#try and except
#risky code inside try block

#the main objective of exception handling is graceful termination or normal termination.

'''try:
    # Risky code here
    
except SpecificError1 as e:
    # Handle specific error 1
    
except SpecificError2 as e:
    # Handle specific error 2
    
except:
    # Handle any other error
    
finally:
    # ALWAYS runs (cleanup code)'''