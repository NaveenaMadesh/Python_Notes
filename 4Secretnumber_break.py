import random #python package random
sn=random.randint(10,20)#randomly chooses the value between these
# random.randrange(10,20)#wont include 20 but randint will
# random.uniform(0,1) # decimal point
print(sn)
for i in range(1,4):
 n=int(input("Enter a number between 10 and 20: "))
 if (n==sn):
  print("Congratulations!!!!You foundd the secret number")
  break
else:
 print("ugh--you lost") 