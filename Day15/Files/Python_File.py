# A python file  is just a text file ending with .py

x = 10
y = 20

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class Calculator:
    def multiply(self, a, b):
        return a * b
#here it automatically gets printed when we import that
#to avoid that I need only when I directly executes the particular file not during the importing
if __name__ == "__main__":
 print("Calculator file loaded!")#executable code
#Every python file has a special variable called __name_


#.py file can contain 
#1.Variables(data)
#2.Functions(reusable codde blocks)
#classes(blueprints for objects)
#Executable code (runs immediately when file is loaded)


