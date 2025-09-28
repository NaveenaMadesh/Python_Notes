name=input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"name : {name}")
print(f"name : {age}")

#conscious here input function accepts all the value as string!!! So the following raises the error
# print(f"Age: {age+5}")
# print(f"Age: {int(age)+5}")
print(f"Age: {age+5}")

#int string to float is possible
#Float string --> integer is impossible
# If I want the user to accept the both float and int use float

# Relational operator or comparision
# here the output is Boolean value but sql uses to filter the data
a = 10
b = 20
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
# print(a>=b)--> (a>b or a==b)
print(a<=b)

# Logical operator:
# and
# or
# not
# print(a==b and a<b)
# print(a>b or a=b)
# or operator both are false then is false
# 
# # memebership operator
# print(10 in(10,20))-->True
# print(10 not in(10,20))-->False

#Identity operator
x=10
y=x
print(id(x))
print(id(y))
print(id(x) is id(y))
# print(10 is 10)-->True
# print(20 is not 10)-->True
x=10
y=10
print(x is y)

x=1000
y=1000
print(x is y)

#False
x = int(input())
Y=int(input())
print( x is Y)

## !!!! is operator checks whether both the object identity are same so it returns false in id(10) is id(10) because it doesnt refer to the value
# dynamic input the value changes 
#literal --> python reuses the object again
#runtime --> here the python allocates different object

# CAN BE USED for checking type as well
print(type(()) is list)

