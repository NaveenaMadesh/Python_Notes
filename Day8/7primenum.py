import math
def prime(n):
    isnot_prime =False
    x= int(math.sqrt(n))
    for i in range(2,x+1):
        if n % i ==0:
            isnot_prime = True
            break
    if isnot_prime is True:
        print("Not prime")
    else:
        print("Prime")

num=int(input("Enter a number: "))
prime(num)
