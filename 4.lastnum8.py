list1 = eval(input("Enter the list of numbers:"))
new_list =[]
for i in list1:
    if i%10 == 8:
        new_list.append(i)
print(new_list)
