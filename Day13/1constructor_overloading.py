#using same name

class Test:

    def __init__(self):
        print("NO args cons")

    def __init__(self,x):
        print("one arg cons")

    def __init__(self,x,y):
        print("Two args cons")


t1 = Test(10,20)

'''Python doesnt supports constructor overloading'''
#there should always one constructor
#if there more than one constructor it considers last constructor
