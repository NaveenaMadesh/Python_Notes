#set is also heterogeneous 
#Order is not preserved 
#indexing and slicing are not supportable
#duplicates are not allowed like list or tuple
s={1,2,20,50,66}
print(s)


#Inserting elements
s.add(70)#add anywhere in the set 
print(s)

#more than one elements
s.update([8,9,10,1])
print(s)

#remove
print(s.remove(1))#return none but modification done at set memory level

#discard
d={1,2,3,4}
d.discard(1)
print(d)
#pop
s.pop()#randomly removes anything
print(s)

#length
print(len(s))


#union
a = {1,2,3,4}
b={3,4,1,2,3}
print("Union:",a | b) # combines eveerything
print("Intersection:",a & b)# common
print("Difference", a - b) # present in a not in b
print("Difference:",b-a)# in b not in a



# for i in s:
#     print(i)


