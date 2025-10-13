#Hiding complex implementation from user for simplicity and security

#we have abstarct class and method
# Abstarction = Force Children to Implement Methods
#concept: Parent class says "You must have this method , but I won't tell you How to Implement it"

'''from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
     def eat(self):
         print("I eat biscuits!!!")

dog = Dog()
dog.eat()'''

# TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'make_sound'
        
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
     def make_sound(self):
         print("I sound bowh,bowh!!!!")

     def eat(self):
         print("I eat biscuits!!!")

dog = Dog()
dog.eat()
dog.make_sound()


# Python won't let you create an object from an abstract class! 
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
     def make_sound(self):
         print("I sound bowh,bowh!!!!")

     def eat(self):
         print("I eat biscuits!!!")

animal = Animal()
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'
# Step 1: Create abstract parent with ABC
# Step 2: Mark methods as @abstractmethod
#         └─> These are RULES, not implementations
# Step 3: Children MUST implement all abstract methods
# Step 4: Can't create objects from abstract class
#         └─> Only from concrete children