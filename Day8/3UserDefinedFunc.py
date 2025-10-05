#User defined function 
#we can write our own function as per our need
#Block of statements or code for repetitive task
#we write functions with arguments
#it executes when it is being called
#To avoid writing a code again and again
#Reduce repeating the code
#ensures code reusability
#lenghth and of code can be reduced and mainatanenece

'''It works when it is being called'''

#Syntax
# def ---> keyword (function definition)
'''def func_name (args):
    statements'''

#Function without parameter
def welcome():
    print("Welcome to python class!!!!")
    # return 

welcome()
# when I use return without returning it also give none--> from this I can understand empty return return returns None
a = welcome()
print(a)#It also returns none
print(welcome())#it expects return value so it prints none as well

#Function with parameter
def welcome(name,age,grade):
    print(f"Welcome to python class {name} and your age is {age},i think you got {grade}")    

# welcome()#Raises type error : requires positional argument

# welcome("Naveena")
# welcome(12)

# positional argument
# welcome("Naveena")#raises error 
welcome("naveena",23,88)


#For changing the order then keyword argument

welcome(age=4,name="Ramya",grade=3)

'''positional argument should not follow keyword but ulta is posiible'''
welcome("Ramya",age=33,grade=90)


#Default argumenet
#we can assign default value to the function

def welcome(name,age=10,grade=12):
    print(f"Welcome to python class {name} and your age is {age},i think you got {grade}")    

#If we dont specify the value then it takes default value
#otherwise the user defined one is taken for account

#Function with return 

def product(x,y,z):
    p=x*z*y
    return p

print(product(1,2,3))

'''always return should be the last one'''

def product(x,y,z):
    p=x*z*y
    q=x*y
    return p,q

print(product(1,2,3))
m,n=product(1,2,3)
print(m,n)

#if I dont want to print but want a value means then we use return
x,y=product(2,3,4)
if x>20:
    print("Eligible")
else:
    print("Not Eligible")


def func(food):
    for x in food:
        print(x)

func(["apple","orange","Banana"])


def func1(f):
    print(f)

func1("Naveena")


def func():
    pass
#There shouldn't be function without statements
#To avoid this we can use pass control sataemnet 

#variable length argument or arbitrary argument
'''*n = zero or more values (optional by nature)'''
'''*n doesn't require any arguments
It can collect zero or more values
If no positional args are given, n becomes an empty tuple ()'''

def sum(*n,name="Raja"):
    sum=0
    for i in n:
        sum+=i
    return sum

a=sum(1,2,3,3)
print(a)
a=sum(name="Naveena")
print(a)

#It is an example for if we havent sspecified a value then it is an empty tuple
def func2(*n):
    return n

print(func2(0))
