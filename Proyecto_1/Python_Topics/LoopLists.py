# You can Loop through the list items by using a for loop:

# print all items in the list, one by one:

fruitList = ["apple", "banana", "cherry"]
for x in fruitList:
    print(x)

# Loop Through the index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
print("\n")
# Print all items by referring to their index number:
listAllFruit = ["mango", "pinaple", "orange"]
for i in range(len(listAllFruit)):
    print(listAllFruit[i])


# Using a While Loop
# Use the len() function to determinate the length of the list, then start at 0 and loop your way through
# the list items by referring to their indexes.

# Remember to increase the index by 1 afeter each iteration.

print("\n")

animals = ["cat", "dog", "cow", "donkey"]
i = 0
while i < len(animals):
    print(animals[i])
    i = i + 1

print("\n")
# Looping Using List Comprehension
# A short hand for loop that will print all items in a list:

furnitures = ["table", "desk", "chair"]
[print(x) for x in furnitures]

print("\n")
# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values
# of an existing list.

# Without List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
print("\n")


# with list comprehesion you can do all that with only one line of code:
# The Syntax
# newlist = [expression for item in iterable if condition == True]

fruitsList = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)
print("\n")

#Python - Sort List 
#Sort List Alphanumerically 
#List object have a sort() method that will sort the list alphanumerically, 
#ascending, by default: 

costaLineFruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
costaLineFruits.sort()
print(costaLineFruits)
print("\n")

#Sort the list numerically 
number_list = [100,50,65,82,23]
number_list.sort()
print(number_list)
print("\n")

#Sort Descending 
#To sort descending, use the keyword argument reverse = True: 
decen_list = ["orange", "mango", "kiwi","pineapple", "banana"]
decen_list.sort(reverse=True)
print(decen_list)
print("\n")

#Sort the list descending: 
des_list = [100,50,65,82,23]
des_list.sort(reverse=True)
print(des_list)
print("\n")

#Customize Sort Function 
#You can also customize your own function by using the keyword argument
#key = function. 
#Example 
#Sort the list based on how close the number is to 50: 

def myfunc(n): 
    return abs(n-80)

lisOrder = [100,50,65,82,23]
lisOrder.sort(key=myfunc)
print(lisOrder)

print("\n")

#Case Insensitive Sort 
#Perform a case-insensitive sort of the list: 
listCase = ["banana","Orange","kiwi","cherry"]
listCase.sort(key=str.lower)
print(listCase)
print("\n")

#Reverse the order of the list items: 
listReverse = ["banana","Orange","kiwi","cherry"]
listReverse.reverse()
print(listReverse)
print("\n")

listCase = listReverse
print(listCase)
print("\n")

#Make a copy of a list with the copy() method: 
thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist)
print("\n")

#Use the list() method 
#Another way to make a copy is to use the build-in method list(). 
anotherList = ["apple","banana", "cherry"]
myAnotherList = list(anotherList)
print(myAnotherList)
print("\n")

#Make a copy of a list with the : operator 
listOperator = ["apple","banana","cherry"]
mylistOperator = listOperator[:]
print(mylistOperator)
print("\n")

#Join Two Lists 

list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)
print("\n")

#appending all the items form list4 into list5 one by one 
list4 =  ["a","b","c"]
list5 = [1,2,3]

for x in list4:
    list5.append(x)
print(list5)
print("\n")

#Use the extend() method to add list2 at the end of list1: 
list5 = ["a","b","c"]
list6 = [1,2,3]
list5.extend(list6)
print(list5)
print("\n")
