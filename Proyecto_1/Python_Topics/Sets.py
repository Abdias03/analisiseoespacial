# Sets are used to store multiple items in a single variable.
# Note: set items are unchangeable, but you can remove items and add new items.

# sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)
print("\n")

# set items
# set items are unordered, unchangeable, and do not allow duplicate values.
# Duplicates Not Allowed
# sets cannot have two items with the same value.
# Duplicate values will be ignored:

# True  and 1 is considered the same value and the values False and 0 are considered the same value:

thisset1 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset1)
print("\n")

# To determine how many items a set has, use the len() function
print(len(thisset1))
print("\n")

# Set items can be of any data type:
# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain diffent data types:
# A set with string, integers and boolean values:
set4 = {"abc", 34, True, 40, "male"}

# What is the data type of a set?
print(type(set4))
print("\n")

# Using the set() constructor to make a set:
thisset2 = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset2)
print("\n")

# Access Items
# You cannot acces items in a set by referring to an index or key
# You can loop through the set items using a for loop, or ask if a specified value is present in a set
# by using the in keyword.

# Loop through the set, and print the values:

thisset3 = {"apple", "banana", "cherry"}
for x in thisset3:
    print(x)

print("\n")

# check if "banana" is present in the set:
print("banana" in thisset3)

# Check if "banana" is NOT present in the set:
print("banana" not in thisset3)

print("\n")

# To add one item to a set use the add() method
thisset3.add("orange")
print(thisset3)
print("\n")

# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("\n")

# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print("\n")

# Remove Item
thisset4 = {"apple", "banana", "cherry"}
thisset4.remove("banana")
print(thisset4)
print("\n")

# Remove "banana" by using the discard() method:
# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
print("\n")

# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
print("\n")

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print("\n")

# The del keyword will delete the set completely:

"""thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
print("\n") """

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("\n")

# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print("\n")

# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
print("\n")

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
print("\n")

# Use | to join two sets:
# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)
print("\n")

# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
print("\n")

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
print("\n")

# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
print("\n")

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)
print("\n")

# You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
print("\n")

# Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
print("\n")

# Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
print("\n")

# You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
print("\n")

# Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
print("\n")

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
print("\n")

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
print("\n")

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
print("\n")

# frozenset is an immutable version of a set.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
print("\n")
