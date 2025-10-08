class Book:
    def __init__(self,title,author,total_copies,available_copies):
            self.title = title
            self.author = author
            self.total_copies = total_copies
            self.available_copies = total_copies
    
    def borrow(self,n):
          if (self.available_copies >= n):
           self.available_copies = self.available_copies - n
           print("Hope you received the book!!!")
          else:
            print(f"Sorry we have {self.available_copies}")

    def returned(self,m):
          self.available_copies = self.available_copies + m
          print("The book returned successfully!!!!!")



book1 = Book("Ponniyin Selvan","Kalki",10)
book1.borrow(5)
print(book1.available_copies)
book1.returned(1)
print(book1.available_copies)
