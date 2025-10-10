#Multilevel inheritance

class Animal:
    leg = 4
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is eating")

class Puppy(Dog):
    def weep(self):
        print("Puupy is weeping")


p=Puppy()
p.eat()
p.bark()
p.weep()