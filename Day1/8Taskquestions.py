# 1. Write the Output of the followings a,b,x,y:
a=x=b=y=235
print(a,b,x,y)

'''Expected : 235 ....Reality: 235'''
# !!!1Huraah

#2.Write the output of the following:
x,y,z,a=1,55,10,23
print(x,y,z,a)

# Expected: 1,55,10,23 = Output

# Write a code for printing datatypes for the following?
A = "Python"
B = 1014
C = 296.12
print(type(A))
print(type(B))
print(type(C))

# Expectation: <class 'str'>,<class int>,<class float> = output

# What Name will be printed in the following code:
Name = 'John'
Name ='Peter'
Name = 'Sam'
print(Name)
print(Name)
print(Name)
#Expected : first--> John, second--> peter , third-->sam
#ud-ooh --output sam for all

# What will be the output for the following?
Name = '‘Johnson’'
Age = 22
Data = Name + Age
print(Data)

# Expectation:Type error = output

# What will be the output for the following?
price = '55'
quantity = 4
Total_Cost = price + quantity
print(Total_Cost)

#Expectation: Type error == output

# What are Variables?
# variables are identifiers which is used to point an object in memory

# 8. If a  =  5; print(‘a’); What will be the output?
a=5
print('a')
# expectation:a

# 9. Name the Datatypes in Python?
'''int,float,str,complex,bool'''

#10. What are the key features of Python?
'''-->High-level
-->portable
-->interpreted
-->Dynamically typed'''

# 11. Which of the following is correct about Python?
# 	A)	Python is a high-level, interpreted, interactive and object-oriented scripting language.
# 	B)	Python is designed to be highly readable.
# 	C)	It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.
'''D)	All of the above.'''

# What gets printed? 
#     print ("Hello" 'F“olks')
'''Hello F'olks'''

# Is python case sensitive?
'''Yes,Python is case sensitive'''

# What type of language is python?
'''When it comes to
Level of abstraction-->High level language
Type checking-->Dynamically typed language
Execution-->Interpreted langauge
Programming paaradigm -->object-oriented,functional,procedural'''

# 15. How is memory managed in Python?
#  Automatic Memory Allocation
# '''''When you create an object (variable, list, etc.), Python automatically allocates memory for it. You don't need to manually allocate or declare memory like in C/C++.'''. Reference Counting
'''''Python keeps track of how many references point to each object in memory.'''
# Garbage Collection
'''Python has an automatic garbage collector that handles circular references (situations where objects reference each other but nothing else references them).'''
#  Memory Pools (Private Heap)
'''Python uses a private heap space to store all objects and data structures. The Python memory manager handles this heap internally. Programmers don't have direct access to it.'''
# . Object Reuse
# Python reuses memory for small integers and short strings to save space:
'''What will be the output?
	number = 5
	number = "five"
	print(number)'''
number = 5
number = "five"
print(number)
# Expected : five =output

# 17. What will be the output?
A = B = C = 10
X = 10
A = X
X = C
B = X
print(A,B,C,X)

# expected : 10 for all = output

# What will be the output?
P = 2; Q=3; R=4
X = P *2 + Q - 2 + R-2
print(X)

# expected:7 = output

'''What is PIP?'''
# Pip installs package -->package manager--> tool that helps you install, upgrade, and manage external libraries/packages that don't come built-in with Python


# 20. What will be the output?
A = 10
A = '10'
A = '10'
B = A + A + A
print(B)
# Type error --- output =101010
