#accessing members of one class inside another class
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
    
    def display(self):
        print("Employee number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee Salary:",self.esal)

class Test:
    def modify(emp):
      emp.esal = emp.esal+10000
      emp.display()

e = Employee(121,"Naveena",10000)
Test.modify(e)