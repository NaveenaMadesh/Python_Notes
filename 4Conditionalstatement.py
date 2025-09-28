# Conditional operator-->if

age = int(input("Enter your age: "))

if(age>=18):
    print("You can vote")

else:
    print("You can't vote")




#multiple conditions
total =300
# students --> 270-300 Grade A 
# students --> 240-269 Grade B
# students --> 200 -239 Grade C 
# students --> <200 Grade D
while True:
 marks = int(input("Enter your marks: "))
 try :
    a = int(marks)
 except :
    raise ValueError("Only integers are allowed")

 if marks >=270 and marks <= 300:
    print("Grade A")
 elif (marks >=240 and marks< 270):
    print("Grade B")
 elif (marks >= 200 and marks < 240):
    print("Grade C")
 elif marks < 200 and marks>=0:
    print("Grade D")
 else:
    print("Please Enter valid input shouldn't be above 300 and negative values")
