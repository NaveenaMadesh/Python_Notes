quiz = {"1":"Ants move in a line because of their sense of ---------",
        "2":"poisonous teeth of the snakes are called as --------",
        "3":"The saltiest water body in the world is ------ sea",
       }

ans = {"1":"smell",
       "2":"fangs",
       "3":"dead"}
score = 0
value1 = input("Enter a number between 1 and 3:")
if value1 in quiz:
    print(quiz[value1])
    ans1 = input()
    if ans1 == ans[value1]:
        print("Correct")
        score +=1
else:
    print("incorrect")

print(score)



# value1=int(input("Enter a number betweeen 1 and 3:"))
# if value1 == 1:
#     print(quiz["q1"])
#     ans=input()
#     if ans == quiz["ans1"]:
#         print("Correct answer")
#     else:
#         print("Incorrect answer")

# elif value1 == 2:
#     print(quiz["q2"])
#     ans=input()
#     if ans == quiz["ans2"]:
#         print("Correct answer")
#     else:
#         print("Incorrect answer")
# else:
#     print(quiz["q3"])
#     ans=input()
#     if ans == quiz["ans3"]:
#         print("Correct answer")
#     else:
#         print("Incorrect answer")



