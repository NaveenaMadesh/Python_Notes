codeword = ["rainbow","butterfly","sunshine","cupcake"]

guess = input("Guess the codeword:").lower()



for i in codeword:
    if guess == i :
        print("You can enter the class")
        break
else:
    print("You can't enter the class!!")

#or 

if guess in codeword:
    print("You can enter the class")
else:
    print("You can't!!!")

    