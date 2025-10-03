countries = input("Enter a list of countries:")

#getting sequence from the user

a="Naveena"
b=list(a)
print(b)

#Here the list function iterates through the string
#Each character becomes a separate list element


a="Singapore,malaysia,pune"
c = list(a)
print(c)


#To get list as a input use eval--> function

list1 = eval(input("Enter the list of countries:"))
new_list = []
for i in list1:
    if len(i)>5:
        new_list.append(i)
print(new_list)
