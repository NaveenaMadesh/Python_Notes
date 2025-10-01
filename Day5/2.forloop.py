#syntax:
'''for variable in iterable
'''
#for loop works with any iterable
#what is an iterable
# iterable is any object that contains multiple items you can loop through one by one.

# 1. range() - generates numbers
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 2. list - collection of items
for i in [10, 20, 30]:
    print(i)  # 10, 20, 30

# 3. string - sequence of characters
for char in "Hello":
    print(char)  # H, e, l, l, o

# 4. tuple - immutable sequence
for item in (1, 2, 3):
    print(item)  # 1, 2, 3

# 5. dictionary - key-value pairs
for key in {"a": 1, "b": 2}:
    print(key)  # a, b

# 6. set - unique items
for item in {1, 2, 3}:
    print(item)  # 1, 2, 3

# 7. file - lines in a file
for line in open("file.txt"):
    print(line)

# for <variable_name> (Temporary label(Your choice)) in <iterable>(what to loop through):
