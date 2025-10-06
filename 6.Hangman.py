import random
words = ["fight","sight","tight","eight"]
random_word=random.choice(words)
print(random_word)
output_list = ['?','?','?','?','?']
life_span = 1

while life_span <= 7:
 print(output_list)
 user_input = input("Guess a character: ").lower()

 if user_input in random_word:
    index = random_word.index(user_input)
    output_list[index] = user_input

 life_span += 1

 if list(random_word)==output_list:
   print("Congratualtions!!! you found the word")
   break
else:
  print(f"Ugh--lifespan completed and the word is {random_word}")
 
 
