def fact(n):
    pro =1
    for i in range(1,n+1):
        pro*=i
    return pro
    

num=int(input("Enter a number:"))
print(fact(num))
