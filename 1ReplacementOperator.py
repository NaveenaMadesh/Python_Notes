name ='Naveena'
sal = 10000
mn='Reema'

print("My name is",name,"and my salary is",sal,".I gave my salary to my mom",mn)

# Since the name is string and the string is we are using we can use "+" operator over there but we could not use the for salary since it is integer
print("My name is"+ name +"and my salary is",sal,".I gave my salary to my mom",mn)
# But one thing is the comma separator leaves the space by default but not the concatenation

#Replacement operaator
print("My name is {} and my salary is {} and I gave it to my {}".format(name,sal,mn))
print("My name is {1} and my salary is {0} and I gave it to my {2}".format(name,sal,mn))
#The below is keyword argument
print("My name is {y} and my salary is {x} and I gave it to my {z}".format(x=name,y=sal,z=mn))

#Formatted string
# %i ==> int type
# %d ==> int type
# %f ==> float
# %s ==> string

print("My name is %s and my salary is %i and I gave it to my %s"%(name,sal,mn))
#we can also use list
n=[1,2,3]
print("My name is %s and my salary is %i and I gave it to my %s"%(name,sal,n))
# another
print(f"My name is {name}")


