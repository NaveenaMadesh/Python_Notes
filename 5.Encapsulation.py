# Encpasulation = Hide the data , only allow access through controlled methods
# Encapsulation = Data is locked in a safe. Only specific methods have the key!

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 🔒 PRIVATE! (double underscore)
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            print(f"Withdrew {amount}")
        else:
            print("Insufficient funds!")
    
    def get_balance(self):
        return self.__balance  # Controlled access!

account1 = BankAccount(1000)
print(account1.get_balance()) 


# Why? Memory explanation:
# player1 -----> [Address 9000:]
#                  ├─ _Player__health: 100  🔒 (Real private attribute)
#                  └─ __health: 0           ❌ (New public attribute created!)
# When you write player1.__health = 0, Python doesn't modify the private __health. Instead, it creates a NEW public attribute called __health!
# The private one (_Player__health) stays 100! 🎯

# Step 1: Make sensitive data PRIVATE (use __)
# Step 2: Create PUBLIC methods to access it (getters)
# Step 3: Create PUBLIC methods to modify it safely (setters)

# class Player:
#     def __init__(self, health):
#         self.__health = health
    
#     # GETTER - Read the data
#     def get_health(self):
#         return self.__health
    
#     # SETTER - Modify with VALIDATION
#     def set_health(self, new_health):
#         if new_health >= 0 and new_health <= 100:
#             self.__health = new_health
#         else:
#             print("Invalid health! Must be 0-100")

