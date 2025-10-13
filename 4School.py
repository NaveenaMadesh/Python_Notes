from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,id_number):
        self.name = name
        self.age = age
        self.id_number = id_number
    
    @abstractmethod
    def introduce(self):
        pass

class Students(Person):
    def __init__(self,name,age,id_number,grade,gpa):
        super().__init__(name,age,id_number)
        self.grade = grade
        self.gpa = gpa


    def introduce(self):
        print(f"Hi I am {self.name} belongs to 12B")

    def can_study(self):
        print("Hi I can able to study!!!")
    
class Teachers(Person):
    def __init__(self,name,age,id_number,subject,salary):
        super().__init__(name,age,id_number)
        self.subject = subject
        self.__salary = salary
        
    def introduce(self):
        print(f"Hi I am {self.name}")

    def can_teach(self):
        print(f"I can teach {self.subject}")

    def salary_view(self):
        print(self.__salary)



s1=Students("Naveena",29,123,'A',90)
T1 = Teachers("Rama",45,1234,"EVS",12000)
s1.introduce()
T1.introduce()
T1.salary_view()
