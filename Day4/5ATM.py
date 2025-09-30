balance = 0
choice = True
while (True):
 choice = input("Enter your choice? D for \"Deposit\" , W for \"Withdraw\,B for \"Balance\",E for \"Exit\"").upper()
 if choice == "D":
   deposited_amount = int(input("Enter the amount: "))
   balance += deposited_amount
   print("The amount successfully deposited!!!")
 elif choice == "W":
   withdraw_amount = int(input("Enter the amount you want to withddraw: "))
   if withdraw_amount > balance:
      print("The amount is greater than balance..Do check your balance !! Then withdraw!!!")
   else:
      balance -= withdraw_amount
      print(f"The amount you withdrawn {withdraw_amount} and the balance is {balance}")
 elif choice =='B':
    print(f"Your Balance is {balance}")

 elif choice == "E":
   break
 
 else:
   continue
 
 again = input("\nPress ENTER to continue or type E to exit: ").upper()
 if again == "E":
    break
print("Thank you for visiting")
