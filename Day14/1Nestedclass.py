#inner class 
#class inside another class
#without exisiting one another cant be exsist

#eg: Class car without Engine
#eg: University without Department


class Outer:
    def __init__(self):
      pass
    def m1(self):
       print("Outer class method!!!")

    class Inner:
       def __init__(self):
          pass
       def m2(self):
          print("Inner class method")

# obj = Outer()
# obj.m1()
# Inobj=obj.Inner()
# Inobj.m2()

# i=Outer().Inner()
# i.m2()


class Human:
   def __init__(self,):
      self.name ="Naveena"
      self.dob = self.DOB()
      
   def display(self):
      print(self.name)
      self.dob.m2()

   class DOB:
    def __init__(self):
          self.DOB = "23/12/1990"

    def m2(self):
       print(f"D.O.B:{self.DOB}")

# Out_Obj = Human()
# Out_Obj.display()
# In_Obj = Human.DOB()
# In_Obj.m2()


class Human :
   def __init__(self,name):
      self.name = name
      self.head = self.Head()
      self.brain = self.Brain()

   def display(self):
      print(f"Name:{self.name}")
      self.head.talk()
      self.brain.think()
    
   class Head:
       def talk (self):
          print("can talk")
        
        
   class Brain:
      def think(self):
         print("can think")

H1=Human("Naveena")
H1.display()

#In python inner classes are independent of outer class !!!!
