# Varible are containers for storing data values

x = 5
y = "John"

# Casting  if you want to specify the data of a variable, this can be done with casting
x = str(3)
y = int(3)
z = float(3)

# Get the Type
# You can get the data type of a variable with the type(). funcion

print(type(x))
print(type(y))

# Single or Double Quotes
# String variable can be declared either by using single o double quotes:
x = "Jhon"
# is the same as
x = 'Jhon'

# Variable names are case-sensitive.
# This will create two variable:
a = 4
A = "Sally"
# A will not overwrite a

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Example

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Camel case

myVariableName = "Jhon"

# Each word starts with a capital letter

MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variable
# python allows you to assign values to multipe variable in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variable
# You can assign the same value to multiple Variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.python allows you to extract the values
# into variables. This is called unpacking

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# In the print() function, you output multiple variables, separated by a comma:
x = "python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome "
print(x + y + z)

# When you try to combine a String and a number with the + operator, python will give you an error:

x = 5
y = "John"
# print(x + y) --> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Global Variable
# Variable that are created outside of a function are known as global variables.
# Global variables can ben used by everyone, both inside of functions and outside.

# Example

x = "awesome"


def myfunc():
    print("Python is" + x)


myfunc()

# Example of create a Variable inside a function, with the same name as the global variable
# Local Variable

x = "awesome"


def myfunc1():
    x = "fantastic"
    print("Python is " + x)


myfunc1()

print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword


def myfunc2():
    global x
    x = "fantastic"


myfunc2()

print("Python is " + x)

# Python Data Type
# Variables can store data of different type, and different type can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type       | str
# Numeric Types: | int, float, complex
# Sequence Types:| list, tuple, range
# Mapping Type:  | dict
# Set Types:     | set, frozenset
# Boolean Type:   | bool
# Binary Type:    | bytes, bytearray, memoryview
# None Type:      | NoneType

x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview
x = None  # NoneType


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	Data Type	Try it
x = str("Hello World")  # str
x = int(20)  # int
x = float(20.5)  # float
x = complex(1j)  # complex
x = list(("apple", "banana", "cherry"))  # list
x = tuple(("apple", "banana", "cherry"))  # tuple
x = range(6)  # range
x = dict(name="John", age=36)  # dict
x = set(("apple", "banana", "cherry"))  # set
x = frozenset(("apple", "banana", "cherry"))  # frozenset
x = bool(5)  # bool
x = bytes(5)  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))


# Python Casting

# Integers:

x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

# Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2

# String:

x = str("s1")  # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes or Three single quotes:

# Example
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Sring are a Arrays
# String in python are arrays of unicode Characters.
# Pythin does not have a Character data type.

# Example
# Get the character at position 1 (remember that the First character has the position 0):
a = "Hello, World!"
print(a[1])

# Looping Through a String
# Since string are arrays, we can lopp through the characters in a string with a for loop.

for x in "banana":
    print(x)

# String Length
# to get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

# check String
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if "expensive" is NOT present in the following text:

txt = "the best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing
# You can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

# Upper case
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# Lover Case
# The lower() method returns the string in lower case:

a = "Hello, world"
print(a.lower())

# Remove WhiteSpace
a = " Hello, World! "
print(a.strip())
# returns "Hello, World"

# Replace String
# the replace() method replaces a string with another string

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
# The Split() method splits the string into substring if it finds instances of the Seprator
a = "Hello, World!"
print(a.split(","))
# returns ['Hello', 'World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# F-String
# F-String was introduced in python 3.6 and now the preferred way of formatting Strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add  curly
# brackets {} as placeholders for variables and other operations.

# Create an f-string

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means
# fixed point number with 2 decimals:
# Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# A placeholder can contain Python code, like math operations:

txt = f"The price is {20 * 59:.2f} dollars"
print(txt)

# Escape Character
# To insert Characters that are illegal in a String, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert

# An example of an illegal character is a double quote inside a String that is surrounded by double Quoetes:

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

# txt = "We are the so-called "Vikings" from the north."
# SyntaxError: invalid syntax

# The escape Character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north"

# Escape Characters

# Code	Result	Try it
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value


# Python Operators
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
# Arithmetic Operators
# Assignement Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

# Operator	Name	        Example
# +	       Addition	        x + y
# -	       Subtraction	    x - y
# *	       Multiplication	x * y
# /	       Division	        x / y
# %	       Modulus	        x % y
# **	   Exponentiation	x ** y
# //	   Floor division	x // y

# Operator	Name	                    Example
# ==	    Equal	                    x == y
# !=	    Not equal	                x != y
# >	        Greater than	            x > y
# <	        Less than	                x < y
# >=	    Greater than or equal to	x >= y
# <=	    Less than or equal to	    x <= y


# Python Lists
mylist = ["apple", "banana", "cherry"]

# List are used to store multiples items in a single variable
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has [0], the second item has index [1] etc.

# print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1[4])

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list

thislist2 = list(("apple", "banana", "Cherry"))
print(thislist2)

# Python Collections (Arrays)

# There are four collection data Type in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable, and unidexed. No duplicate members.
# Dictionary is a collection which is ordered and changeable. No duplicate members.

# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change intem Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# To insert a new item, without replacing any of the existing values, we can use the insert(). method
# the insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Add List Items
# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.
thislist1 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist1.extend(tropical)
print(thislist1)

# Remove Specified Item
# The remove() method removes the specified item
thislist2 = ["apple", "banana", "cherry"]
thislist2.remove("banana")
print(thislist2)
# if there are more than one item with the specified value, the remove() method removes the first occurrence

# Remove Specified Index
# The pop() method removes the specified index
listToRemove = ["apple", "banana", "cherry"]
listToRemove.pop(1)
print(listToRemove)
# if you do not specify the index, the pop() method removes the las item.

# The del keyword also removes the specified index:
# Remove the first item
removeTheFirstItem = ["apple", "banna", "cherry"]
del removeTheFirstItem[0]
print(removeTheFirstItem)

# The del keyword can also delete the list completely.
listDelete = ["apple", "banana", "cherry"]
del thislist

# Clear the List
# The clear() method empties the list.
# the list still remains, but it has no content.
listclear = ["apple", "banana", "cherry"]
listclear.clear()
print(listclear)
