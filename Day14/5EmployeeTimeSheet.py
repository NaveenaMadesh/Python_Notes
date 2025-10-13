class Employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal

    def __mul__(self,other):
        return self.sal * other.days
    
class Timestamp:
    def __init__(self,name,days):
         self.name = name 
         self.days =days

    def __mul__(self,other):
        return self.days * other.sal
        
e1 = Employee("Naveena",2000)
t1 = Timestamp("Naveena",10)
print(e1*t1)
print(t1*e1)