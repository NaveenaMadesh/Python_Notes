stock = {
    "banana": 10,
    "apple": 15,
    "orange":12,
    "pear":15
}

price={
    "banana":20,
    "apple":80,
    "orange":60,
    "pear":90
}

shoplist = stock.copy()
print(shoplist)
price1 = 0
for i in shoplist:
 value1=int(input(f"Enter the quantity of {i}: "))
 if value1 <= shoplist[i]:
  shoplist[i] = value1
  price1 += price[i]* value1
 else:
  print(i,"Out of stock!!!")
print(shoplist)
print(price1)

