#Multiple --> Many parents 
#overriding parent and child has same method name
class P1:
    def m1(self):
        print("Parent1 class Method m1")

class P2:
    def m1(self):
        print("Parent2 class method m1")

class P3:
    def m1(self):
        print("Parent3 class method m3")

class C(P1,P2,P3):
       def m1(self):
        super().m1()
        print("Child class method m1")

obj = C()
obj.m1()