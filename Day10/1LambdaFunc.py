#Laambda functions are anonymous function
#Nameless function
#defined in a single line no need of return statemene
#for one time use
#take any number of args but one expression

#Syntax: variable_len = lambda args1...args2:exp(returns)

def f(n):
    return lambda a:a*n

x=f(2)
print(x(11))


x=lambda b:b+100
print(x(4))


s1="welcome"
s=lambda s1:s1.upper()
print(s(s1))

prod = lambda a,b:a*b
print(prod(2,3))

p=(lambda a,b : a*b) (7,3)
print(p)

#keyword argument
p=lambda a,b : a*b
print(p(b=10,a=5))


#default value
p=lambda a=10,b=5 :a*b
print(p(20,10))

#variable length keyword argument
p=lambda **a : print(a)
p(a=10,b=10)

#variable-length argument

p=lambda *a : print(a)
p(10,20,30,40)

#higher order function
#function which receives another function as an object means that is lambda function!!!!!
hof = lambda x,func : x+func(x)
print(hof(2,lambda x:x*x))

op =(lambda x:(x%2 and "odd" or "Even"))(38)
print(op)

substr =  lambda string : string in " welcome to Python"
print(substr("come"))

#input from user
n=int(input("Enter a number:"))
sqr = lambda b:b**2
cube = lambda b:b**3

print(sqr(n),cube(n),end="\n")

#filter --> can use it in lambda 
#when we use * infront of variable it prints only the value
'''Filter works in the way : it pases each and every element into the lambda then 
the lambda evaluates whether it is true or false then
finally it provides the tuple and it wont perform untill we creates a tuple or list
it only creates object'''
num = [20,10,3,45,60]
x = filter(lambda a: a%2==0 , num)
print(*(list(x)))

a=(1,2,3)
print(*a)

#map function
#value applicable to all the elements in sequence
'''How map works map passes each element into lambda and replaces 
the exsisting values and one more thing it just creates object untill we uses tuple or list'''
l1 = (10,20,30,40,50)
double = tuple(map(lambda x: x*2,l1))
print(double)

#reduce 
#reduce to one 
#reduce works in two elemeents
#here the it performs pair beacuse we can use this for any limit regardless of list size
#here it is used where we have default product function!!!
from functools import reduce
list1 =[1,2,3]
sum = reduce((lambda x,y : x+y),list1)
print(sum)
#accumlator --> x

def quad(a,b,c):
    return lambda x : a*x**2 + b*x+c

f=quad(2,3,4)
print(f(3))
    
#with conditional statements
c=lambda x: x*2 if x<3 else x*5
print(c(2))
