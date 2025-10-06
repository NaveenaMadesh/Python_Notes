#if I dont know how many keyword argument I am going to pass then I will use arbitrary keyword argument function
'''**kwargs'''
'''Here there will be no positional args are allowed 
'''
def display(**x):
    print(type(x))
    print("Record information")
    for k,v in x.items():
        print(k,"....",v)
    return x ,x.keys()


x,y=display(name="Naveena",age=89)
print(x)
print(y)
#here the items is a view object