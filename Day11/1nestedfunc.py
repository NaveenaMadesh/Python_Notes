def f1():
    x="Ramya"
    def f2():
        x ="Hello"
        return x
    f2()
    return x

print(f1())#Ramya

#nonlocal
def f1():
    x="Ramya"
    def f2():
        nonlocal x
        x ="Hello"
        return x
    print(f2())
    return x

print(f1())#Ramya
