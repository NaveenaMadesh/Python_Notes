# break:

for i in range(1,101):
    if(i==5):
        break
    print(i)

# It loops till the condition is true when it is true then loop gets break

for i in range(1,10):
    print(i)
    if (i==5):
        break
# we cannot use break outside the loop
# after break it comes outside and starts executing the line outside the loop

'''Continue'''

for i in range(1,10):
    if(i==5):
        continue
    
# continue skip the current iteration then jumps to next

# why we need break :

# guess a number between 10 and 15
# find the secret number only 3 chances 