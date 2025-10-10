class Student:
    school = "XYZ" #static
    def __init__(self,name,age):
        self.name = name
        self.age=age


s1=Student("Naveena",23)
s2=Student("Kasi",123)
s1.school = "MMM"#it reflects only on particular objects not for all objects..
print(s1.school)
print(s2.school)


# here it creates new instance variable in s1 the static variable remians same !!
