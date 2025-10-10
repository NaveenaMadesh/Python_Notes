#Single inheritance

class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
  
     def bark(self):
         print("Dog is barking")


a=Dog()
a.eat()
