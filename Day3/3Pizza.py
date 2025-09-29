print("Welcome to pizza hut !!! Kindly choose what kind of pizza you want!!!")

pizza_type = input("Enter the you want veg or non-veg: ").lower()

if(pizza_type == 'veg'):
    pizza_wanted = input("Enter whether you want palm house or deluxe veg: ").lower().replace (" ","")

    if(pizza_wanted == 'palmhouse'):
        print("The cost of palm house is  300")
    elif (pizza_wanted == 'Deluxeveg'):
        print("The cost of deluxe veg is 500")
    else:
        print("Sorry, the pizza you entered here is not available.")
else:
        pizza_wanted = input("Enter whether you want chicken sausage or mutton sausage: ").lower().replace("","")

        if(pizza_wanted == 'chickensausage'):
             print("The cost is 500")

        elif(pizza_wanted == 'muttonsausage'):
             print("The cost is 300")
        else:
             print("The pizza you entererd is not available!!please refer the menu!!!")
              
