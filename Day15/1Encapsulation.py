#Encpasulation --> Binding data and method
#restricts direct access to certain data 
#data hiding --> keeping the variable and methods in private
# we can access through method

#restricting the access of the method and data from other classes (inheritance)

#access modifiers
#public can access anywhere!!!!!!
# name = public 

#protected 
#accessed within the class and child class
# '''_name '''(single_und)

#private
#prefix with __(dund)
#cant access outside the class

#data members attri and methods in class 


#protected here the varaiable can be used in class and sub class
class Base:
    def __init__(self):
        self._a =2 #protected 
        self.c ="Hello"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self._a)
        self._a = 3
        print(self._a)

# d = Derived()
# b = Base()
# print(b._a)
# print(d._a)


#Private
#We cannot access outside this class
class Base:
    def __init__(self):
        self.__a =10#private 
        self.c ="Hello"
    
    def Base_view(self):
        print(self.__a)
    
    def modifiy(self,n):
        if n>0 and n<1000000:
            self.__a = n
            print(self.__a)

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self.__a)
        self._a = 3
        print(self.__a)

# d = Derived()
b = Base()

b.Base_view()
b.modifiy(20)
b.Base_view()
# print(b.__a)

# print(d.__a)



