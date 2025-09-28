# units 0-100 --> cost : rupees 2
# units 101-200 --> cost : rupees 3
# units 201-300 --> cost : rupees 4
# units 301 -500 --> cost : rupees 5
# units >=500 --> cost : rupees 8

units = int(input("Enter the units consumed: "))
try :
    a = int(units)
except:
    raise ValueError("Provide only integer data")

if units >= 0 and units <= 100:
    print(f"Price : {units * 2}")
elif units >= 101 and units <= 200:
    print(f"price {units*3}")
elif units >=201 and units <= 300:
    print(f"price {units*4}")
elif units >=301 and units <=500:
    print(f"price {units*5}")
elif units >= 500 and units <=0:
    print(f"price {units*8}")
else:
    print("Please enter valid input")