#unpacking

coordinates = [10,20]
x,y = coordinates
print(x)#10
print(y)#20

#The rule : Number of variables on left must match number of items on right!
#Valueerror : too many values to unpack (expected 2)
a,b=[1,2,3]
print(a)
print(b)

a,b,c = [1,2]
print(a)
print(b)
#valueerror : not enough values to unpack

# 2.The * operator - Extended unpacking

numbers=[1,2,3,4,5]

first,*rest=numbers
print(first)
print(rest)

first, *middle, last = numbers
print(first)
print(middle)
print(last)


# packing
def sum_all(*numbers):
    print(type(numbers))
    print(sum(numbers))

result = sum_all(1,2,2,3,4)
print(result)


#swapping 
a,b = 10,20
a,b = b,a
print(a,b)