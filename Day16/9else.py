try:
    number = int(input("Enter a number: "))
    result = 100/number

except ValueError as e:
    print(f"Not a number {e}")

except ZeroDivisionError as e:
    print(f"Enter other value than 0 {e}")

else:
    print("Sucess!!!")

finally:
    print("Cleanup code")



try:
    # Put ONLY the risky code here
    x = 10 / 2
    
except ZeroDivisionError:
    print("Division error!")
    
else:
    # Put success celebration code here
    print("Division worked!")
    # Code here is NOT protected by except above




    # Create alarm
class NameTooShortError(Exception):
    pass

# Function that checks name
def register(name):
    if len(name) < 3:
        raise NameTooShortError("Name must be 3+ letters!")  # Ring alarm!
    print(f"Welcome {name}!")

# Try it
try:
    register("e")  # Too short! Will ring alarm!
except NameTooShortError as e:
    print(f"ERROR: {e}")