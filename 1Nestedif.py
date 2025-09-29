# Nested if is one if inside another if
# if(condition): if true next if
#     if(condition): this 
#         ....
#         .....
#         ....
#     else:
#         .....
#         .....
# else:
#   ..... (if 1st if condition is false then it comes here)

name = input("Enter your name : ")
country = input("Enter your country: ").capitalize()

if(country == 'India'):
    age = int(input("Enter your age: "))
    if(age >= 18):
        print("You can vote")
    else:
        print("You can't vote")
else:
    print("You should be an India to vote")





