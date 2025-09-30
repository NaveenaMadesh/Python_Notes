# printing 1 to 5
#use end ="" because python default it takes as newline character
# for i in range(1,6,1):
#     print(i,end=" ")

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

for i in range(1,6):
    for j in range(1,6):
        print(j, end="")
    print()

#1 1 1 1 1
#2 2 2 2 2
#3 3 3 3 3
#4 4 4 4 4 

for i in range(1,5):
    for j in range(1,5):
        print(i,end =" ")
    print()

#1
#1 2
#1 2 3
#1 2 3 4

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# 4 3 2 1
# 3 2 1
# 2 1
#1

for i in range(1,5):
    for j in range(4-i+1,0,-1):
        print(j,end="")
    print()
