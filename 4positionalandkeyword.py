# Great question! Let me break down how Python handles positional and keyword arguments.
# How Python Maps Arguments
# Positional arguments are mapped by their position/order:
# pythondef greet(name, age):
#     print(f"{name} is {age} years old")

# greet("Alice", 25)  # name="Alice", age=25
# Keyword arguments are mapped by their name:
# pythongreet(name="Bob", age=30)  # explicit mapping
# greet(age=30, name="Bob")  # order doesn't matter!
# Why Keyword Args Can't Follow Positional Args? They Can!
# Actually, keyword arguments CAN follow positional arguments. What you can't do is have positional arguments follow keyword arguments.
# ✅ Valid - Keywords after Positionals:
# pythongreet("Charlie", age=35)  # perfectly fine!
# ❌ Invalid - Positionals after Keywords:
# pythongreet(name="David", 40)  # SyntaxError!
# Why This Restriction Exists
# Python processes arguments left to right:

# Positional args are assigned to parameters by position
# Keyword args are assigned to parameters by name

# If you allowed positionals after keywords, it creates ambiguity:
# pythondef func(a, b, c):
#     pass

# func(b=2, 1, 3)  # What would this mean?
# # Does 1 go to 'a'? But we skipped 'a' with the keyword arg
# # This is confusing and ambiguous!
# Once Python sees a keyword argument, it no longer knows which position you're at in the parameter list. Allowing positional args after would make the mapping unclear.
# Special Parameter Types
# Python also has special syntax to control this:
# pythondef func(a, b, /, c, d, *, e, f):
#     pass

# # a, b: positional-only (must come before /)
# # c, d: can be positional or keyword
# # e, f: keyword-only (must come after *)

# func(1, 2, 3, d=4, e=5, f=6)  # valid
# func(1, 2, c=3, d=4, e=5, f=6)  # valid
# func(a=1, b=2, c=3, d=4, e=5, f=6)  # invalid - a,b must be positional
# The rule keeps Python's argument resolution simple and unambiguous!