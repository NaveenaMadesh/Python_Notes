#variables --> Global and local
#the place where we are using the variable
#based on where we are creating a varible the accessibility decidedd
#local 

# declaring variable outside function definition
# a=10#(global variable)
def func():
    a=20#(local variable)
    print(a)

def func2():
    print(a)

func()
func2()


def f1():
    a=10
    print(a)

# print(a)#cannot access the local variable outside the function
f1()


a=67
def f5():
    a=10
    print(a)

print(a)#67
f5()#10


#here first checks inside the function
#then it goes to global variable
a=67
def f7():
    b=45
    print(a)
    print(b)
print(a)
f7()


#here the local values takes 
a=67
def f7():
    a=10
    b=45
    print(a)
    print(b)
print(a)
f7()

#with function argument
a=67
def f7(b):
    b = 45
    print(a)
    print(b)

print(a)
f7(10)#priority goes to local variable in case of b


a=67
def f1():
    global a
    a=25
    b=23
    print(a)
    print(b)

f1()#Here we are chnaging global variable to local
print(a)
f1()


a=67
def f1():
    # global a
    a=25
    b=23
    print(a)
    print(b)

f1()#Here we are chnaging global variable to local
print(a)#67 global -> local replacemnet wont take place
f1()

#In oops class if we have multiple functions the local variable of one method cant be used in anyother method

