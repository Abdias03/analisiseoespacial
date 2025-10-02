"""
Dictionaries are used to store data values in key: value pairs. 
A dictionary is a collection which is ordered*, changeable and do not allow duplicates. 
As of Python version 3.7, dictionaries are ordered. In python 3.6 and earlier, dictionaries are unordered 
"""
# Dictionaries are written with curly brackets, and have keys and values:


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print("\n")

# print the "brand" value of the dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print("\n")

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# Print the number of items in the dictionary:
print(len(thisdict))
print("\n")

# The values in dictionary items can be of any data type:
# String, int, boolean, and list data types:

thisdict1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict1)
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
print(type(thisdict))
print("\n")

# Using the dict() method to make a dictionary:

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
print("\n")

# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:
x = thisdict.get("brand")
print(x)

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)
print("\n")

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change
print("\n")

# The values() method will return a list of all the values in the dictionary.
x = car.values()
print(x)


# The items() method will return each item in a dictionary, as tuples in a list.
x = car.items()
print(x)
print("\n")

# heck if "model" is present in the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print("\n")

# Change Dictionary Items
thisdict["year"] = 2018
print(thisdict)
print("\n")

# Update the "year" of the car by using the update() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print("\n")
# Update puede actualizar varios valores a la Vez
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

thisdict.update({"year": 2020, "color": "red"})
print(thisdict)
print("\n")
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removed the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)
print("\n")
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)
print("\n")
# The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)
print("\n")
# The del keyword can also delete the dictionary completely:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# del thisdict
# this will cause an error because "thisdict" no longer exists.
print(thisdict)
print("\n")

# the clear() method empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# thisdict.clear()
# print(thisdict)

# print all key names in the dictionary, one by one:
for x in thisdict:
    print(thisdict)
print("\n")
# print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
print("\n")

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)
print("\n")
# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)
print("\n")
# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will
# only be reference to dict1 and changes made in dict1 will automatically also be made in dict2.

# Make a copy of a dictionary with the copy() method:
thisdict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict3.copy()
print(mydict)
print("\n")

# Another way to make a copy is to use the built-in function dict().
# Make a copy of a dictionary with the dict(). function:

thisdict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydictionary = dict(thisdict3)
print(mydict)
print("\n")

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child2"]["name"])
print("\n")

# Loop Through Nested Dictionaries
# Loop through the keys and values of all nested dictionaries:

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

print("\n")
