fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("\n")

# Loop through the letters in the word "banana":

for x in "banana":
    print(x)
print("\n")

# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print("\n")

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print("\n")

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print("\n")

# Using the range() function:

for x in range(6):
    print(x)
print("\n")

# Using the start parameter:

for x in range(2, 6):
    print(x)
print("\n")

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
    print(x)
print("\n")

# Nested Loops
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
print("\n")
