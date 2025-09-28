"""
Tuples are used to store multiple item in a single variable. 
Tuple is one of 4 build-in data type in python used to store collections
of data, the other 3 are List,Set, and Dictionary, all with different 
qualities and usage.
A tuple is a collection which is ordered and unchangeable 
Tuples are written with round brackets. 

"""

#Create a Tuple: 
thistuple = ("apple","banana","cherry")
print(thistuple)
print("\n")

#Tuple items are ordered, unchangeable and allow duplicate values. 
#Tuple items are indexed, the first item has index [0], the second 
#item has idex [1]
#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print("\n")

#Print the numberof items in the tuple: 
thistuple1 = ("apple","banana","cherry")
print(len(thistuple1))
print("\n")

#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))
print("\n")

##NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print("\n")

#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
print("\n")

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print("\n")

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""
#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
#Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Check if "apple" is present in the tuple: 
thistuple2 = ("apple","banana","cherry")
if "apple" in thistuple2:
    print("Yes, 'apple' is in the fruits tuple")
print("\n")


#Workaround 
#Change Tuple Values 
#Convert the tuple into a list to be able to change it: 
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print("\n")

#Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
print("\n")

#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
print("\n")

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
print("\n")

#this will raise an error because the tuple no longer exists
#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) 

#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print("\n")

#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
print("\n")

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
print("\n")

# Loop Tuples 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
print("\n")

#Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
print("\n")