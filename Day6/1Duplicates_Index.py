a = [1,2,3,4,1]
print(a.count(1))
first_index = a.index(1)
print(first_index)
second_index = a.index(1,first_index + 1)
print(second_index)

a.pop(second_index)
print(a)

# sherin's approach 
# convert to set because set doesn't allow duplicates
a=[1,2,3,4,5]
b= set(a)
print(b)

a = list(b)
print(a)

s=[]
print(type(s))

s={}
print(type(s))
