"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
# if statement:
a = 33
b = 200

if b > a:
    print("b is greater than a")
print("\n")
# python relies on identation (whitespace at the beginning of a line) to define scope
# in the code. Other programming languages often use curly-brackets for this purpose.

# ELif
# The elif keyword is python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
print("\n")
# Else
# The else Keyword catches anything which isn´t caught by the preceding conditions.

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
print("\n")
# Short Hand if
# if you have only one statement to execute, you can put it on the same line as the if statement.

# One line if statement:
if a > b:
    print("a is greater than b")
print("\n")

# One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")
print("\n")

# You can also have multiple else statements on the same line:
# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print("\n")

# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
print("\n")

# The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
print("\n")

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
print("\n")
# you can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
print("\n")
# The pass Statement
# if statements cannot be empty, but if you for some reason have a if statement with no content, put in the pass
# statement to avoid getting an error.

a = 33
b = 200

if b > a:
    pass
print("Nothing Happend ", "\n")

# Python Match
# The match statement is used to perform different actions based on different conditions.

# The python Match Statement
# The match expression is evaluated once.
# The value of the expression is compared with the values of each case.
# If there is a match, the associated block of code is executed.

# The example below uses the weekday number to print the weekday name:

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:  # Character _ as the last case value if you want a code block to execute when there are not other matches:
        print("Looking forwar to the Weekend")
print("\n")

# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
print("\n")
# You can add if statements in the case evaluation as a extra condition-check:

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
print("\n")
