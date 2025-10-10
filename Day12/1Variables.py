# using self we are accessing and declaring instance variable
#instance , static, local
#local--> declare any variable inside methodd can only used inside that method

'''class classname:
 common_variable = "....."#static it is common for all object because of this we can save the memory!!!!
 def __init__(self):
    self.name = name #instance variable --> it varies from obj to obj

def speak(self):
    x=10#inside method --> can be accessed within the method
    print(x)#no need of self.x an all because it is common for all

'''
#count,#instance
'''class classname:
   def __init__(self,count=0):
      self.count = count
      self.count +=1

   def get_count(self):
      print(self.count)

class1 = classname()
class1.get_count()'''



'''#static
class classname:
   count=0
   def __init__(self):
      classname.count = classname.count
      classname.count +=1

   @classmethod # decorator
   def get_count(cls):
      print(cls.count)

class1 = classname()
class1.get_count()
class2 = classname()
class2.get_count()
class3 = classname()
class3.get_count()'''



class Student:
   college ="IIT"
   princy = "Naveena"

   def __init__(self,name,age,id):
     self.name = name
     self.age = age
     self.id = id

   #instance method(atleast one instance veriable inside the method then it is instance method)
   def m1(self):
      m=10
      for i in range(m):
         print(i)

   #instance method
   def talk(self):
      print(f"Hi I am {self.name}")
      print(f"My age is {self.age}")
      print(f"ID:{self.id}")
      print(Student.college)
    #   print(cls.college) can't do this
   
   @classmethod
   def getcollegeinfo(cls):
      print(cls.college)
      print(cls.princy)
    #   print(self.name)#can't do this
      
    
   @staticmethod #no obj or classs 
   def avg(a,b,c):
      return(a+b+c)/3
   


s1= Student("Naveena",12,1234)
# print(s1.name,Student.college)
# Student.getcollegeinfo()
# s1.talk()
# print(s1.avg(1,2,3))
# print(Student.avg(1,2,4))
# print(avg(1,2,3)) not works
s1.getcollegeinfo()
Student.getcollegeinfo()



'''if we use atleast one instance variable we need to use self and for instance method we dont need decorator'''
'''if we take class method --> using only static variable!!!'''
'''we need to use decorator classmethod first argument should be cls'''
'''inside instance we can use bith instance and static but inside class we can only have class variable!!!'''
'''we can also call class method using object name or by using class name '''
