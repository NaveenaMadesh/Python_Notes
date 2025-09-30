count = 0
total =0
price =True
while (price!=0):
  price = int(input("Enter the price of goods.type 0 to stop: ")) 
  if price !=0:
   total+=price
   count+=1
print(f"Total number of goods are {count} and the total price {total}")
