# print(3+4)
# print("3"+"4")
# l1=[]
# l2=[]
# print(l1+l2) 

#same operator but shows different behaviour

'''we cannot add two objects!!!! using binary +'''

class Total:
    def __init__(self,pages):
        self.pages = pages  
    
    def __add__(self,other):
        sum = self.pages + other.pages
        t1 = Total(sum)
        return t1
        # return Total(self.pages + other.pages)

    def __mul__(self,other):
        mul = self.pages*other.pages
        t2 = Total(mul)
        return t2
    
    def __sub__(self,other):
        sub = self.pages-other.pages
        t3 = Total(sub)
        return t3
    
    def __lt__(self,other):
        t3 = self.pages < other.pages
        return t3
    
    
    def __str__(self):
        return "The number of pages :" + str(self.pages)#to avoid printing the object memory adress
        #automatically called when we print() aan object
t1 = Total(100)
t2 = Total(200)
t3 = Total(300)
print(t1 + t2)
print(t1+t2+t3)
print(t1*t2)
print(t1*t2*t3)
print(t1 - t2)
print(t1-t2-t3)
print(t1<t2)


# here we are passing the memory address of two variable then we are adding the both object's attribute
# then it return new address actually
# how it works in t1+t2+t3 ==> t1.add(t2)--> return an object --> result we are trying to add integer
'''Python supports operator overloading .method and constructor overriding'''