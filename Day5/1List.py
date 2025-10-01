# Data structure is way of structuring the data
#It is used to store n number of values in single variable
#In other programming langauage we call list as an array
#Array is known as collection of similar data types

'''
As per documentation
A data structure is a way to store data and having particular methods to retrieve or manipulate it.
It comes under both data types and data structure as it defines what kind of data it is as well it also defines how it organizes the data..
List holds heterogeneous objects
Data structure organizes group of data and have some tecniques to retrive an manipulate

'''
#Syntax
a=[]
#For number
a=[1,2,3]
a=[1,'red',3,4.5]

#access those elements 
# Using index

#Slicing-->
s="Welcome to python class"
print(len(s)) #-->prints including the sapce

#To print particular character
print(s[8])
#we can use index the index always starts with 0 


#To slice a range---> from index 3 to 7
# s[start:end:step]-->all are optional 
# default start -->0 , step--> 1, stop--> till end of the string
#[]--> represents indexing or accessing!!!
print(s[:7])
print(s[:7:2])
print(s[::])
print(s[3::2])
print(s[:5:3])

#negative
print(s[-1::]) #ans:s
print(s[-4::]) #ans: lass
print(s[-2:0]) # wont print anything
#how the negative indexing works--> end value starts as -1 indexing then -3 meand includes values from last value when no end value specified 
#If I want to specify the end value it should be negative when I gives positive then it wont print anything
#and it wont includes the last letter when it comes metioning by default start and end value

print(s[-1:-1]) #prints nothing
print(s[::-1]) # reverses the string 
#Here the start position is last and moves forward towards left

print(s[1:5:-1])#prints nothing

# List is ordered collection of data
# List is mutable -->changeable we can change once we create modify add ,remove
#Items in list are need not to same data type
#use []
#Insertion order will be preserved
#Indexing and slicing concepts are allowed
#duplicate objects are allowed
#scalable
#no end value consider in slicing's end value

fruits=["apple","banana","orange","kiwi","papaya","melon","orange","apple"]
print(len(fruits))
print(id(fruits))
print(fruits)
# print(fruits[8])#Indexerror
print(fruits[len(fruits)-1])

#replacing
fruits[0]="banana"
print(fruits)
#In the above case the first value gets replaced by this value

for x in range(0,len(fruits)):
    print(x)
ans:0
'''1
2
3
4
5
6
7'''

for x in range(0,len(fruits)):
    print(x," ",fruits[x])

for x in fruits:
    print(x)
'''banana
banana
orange
kiwi
papaya
melon
orange
apple'''

if "apple" in fruits:
    print("Apple is there")
else:
    print("not in")

#Adding new elemeents
#appendd--> end of the list
#syntax:
# fruits.append()
fruits.append("Avacado")
#can add only one
'''assignment operator replace the exsisting one'''
#Want to add more than one
fruits.extend(["kiwi",'pine'])
print(fruits)
#the extend also inserts at the end

#index
print(fruits)
print(fruits.index("orange"))
print(fruits.count("orange"))

#insert 
#insert at other than end
print(fruits)
fruits.insert(4,"litches")#just moves the already exsisting towards right
print(fruits)


#remove #here index alone not works
'''fruits.remove([1])#error'''
fruits.remove("apple")
print(fruits)
fruits.remove("orange")
print(fruits)#If duplicates are there it only removes the first one

#pop
fruits.pop(3)
print(fruits)
fruits.pop()
print(fruits)

#copy
myfruits = fruits.copy()

#clear the entire values at one instance
fruits.clear()
print(fruits)

del fruits #Completely deletes the list along with structure
print(fruits)#Name error

# conactenation
# list3 = list1+list2

# for x in list1:
#     list2.append(x)
# print(list2)

#list1.eextend(list2)
# print(list1)

# fruits.sort(reverse = False)--> ASc
# print(fruits)
