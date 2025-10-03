t = 10
print(type(t))#int
print(t)

t=()
print(type(t))#tuple

t =(3+5+6)
print(type(t))#int

t=(10)
print(type(t))#int

t=(10,)
print(type(t))#tuple

#immutable --> you cannot change an existing object in memory but can create a new object
#Tuple is immutable
#Duplicates are allowed 
#heterogeneous data are allowed
#insertion order is preserved 
#indexing and slicing will work

t=10,20,30,40
print(len(t))
print(t[3])
#slicing works

print(t[len(t)-2])#30

t3 = t + (1,2,3,4)
print(t)

#max
print(max(t))
print(min(t))
print(sum(t))

#Error(mutablility check)
'''t[2] = 45
'''#Type error :Tuple object does not support item assignment

#iteration:
for i in range(0,len(t)):
    print(t[i])

'''If I want to modify the data in tuple convert it to list then do modify then convert back to the tuple'''

