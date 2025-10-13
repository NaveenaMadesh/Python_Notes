#access modifier --> private, protected(can't use in another class inside that program (can't do using import)) , public
#data hiding
class car:
    def open_door(self):
        print("Door Opened")
        self._accelerate()
        self.__engine()

    def _accelerate(self):#can access in another module!!!
        print("Throttle Increase")

    def __engine(self):
        print("Burst Inside\n Car is moving")
    
    def view_engine(self):
        self.__engine()

c=car()
c.open_door()
# c.open_door()
# c._accelerate()
# c.__engine()#Attribute error
# c.view_engine()
