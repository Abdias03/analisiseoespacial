# A function is a block of code which only runs when it is called.
# You can pass data,known as parameters, into a function.
# A function can return data as a result.

# In Python a function is defined using the def keyword:

def my_fuction():
    print("Hello from a function")
    print("\n")


# To call a function, use the function name followed by parenthesis:
my_fuction()

# Arguments are specified after te function name, inside the parantheses. You can add as many arguments
# as you want, just separate them with a comma.


def my_function(fname):
    print(fname + " refsnes")


my_function("Email")
my_function("tobias")
my_function("Linus")
print("\n")
# This function expects 2 arguments, and gets 2 arguments:


def my_function1(fname, lname):
    print(fname + " " + lname)
    print("\n")


my_function1("Emil", "Refsnes")

# If you try to call the function with 1 or 3 arguments, you will get an error:

# Arbitrary Arguments, * args
# if you do not know how many arguments that will be passed into your function, add a * before the
# parameter name in the function definition
# This way the function will receive a tuple of arguments, and can access the items accordingly:


def myFunction(*kids):
    print("The youngest child is " + kids[2])
    print("\n")


myFunction("Email", "Tobias", "Linus")

# You can also send arguments with the key = value syntax.


def my_function_2(child3, child2, child1):
    print("The youngest child is " + child3)
    print("\n")


my_function_2(child1="Emil", child2="Tobias", child3="Linus")

# If the number of keyword arguments is unknown, add a double ** before the parameter name:


def my_function_3(**kid):
    print("His last name is " + kid["lname"])
    print("\n")


my_function_3(fname="Tobias", lname="Refsnes")

# The following example shows how to use a default parameter value.


def my_function3(country="Norway"):
    print("I am from " + country)
    print("\n")


my_function3("Sweden")
my_function3("India")
my_function3()
my_function3("Brazil")

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:


def my_function_4(food):
    for x in food:
        print(x)


fruits_tropical = ["apple", "banana", "cherry"]
my_function_4(fruits_tropical)
print("\n")

# To let a function return a value, use the return statement:


def my_function_data(x):
    return 5 * x


print(my_function_data(3))
print(my_function_data(5))
print(my_function_data(9))
print("\n")

# The pass Statement


def myfunction():
    pass

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.


def my_function_pass(x, /):
    print(x)


my_function_pass(3)

# To specify that a function can have only keyword arguments, add *, before the arguments:


def my_function_5(*, x):
    print(x)


my_function_5(x=3)

# You can combine the two argument types in the same function.


def my_function_6(a, b, /, *, c, d):
    print(a + b + c + d)
    print("\n")


my_function_6(5, 6, c=7, d=8)

# Recursion

"""
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

"""


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)

print("\n")


def tri_recursion_print(k, nivel=0):
    print("  " * nivel + f"Entrando a tri_recursion({k})")

    if k > 0:
        result = k + tri_recursion_print(k - 1, nivel + 1)  # llamada recursiva
        print("  " * nivel +
              f" Saliendo de tri_recursion({k}) con resultado = {result}")
    else:
        result = 0
        print("  " * nivel +
              f"Caso base alcanzado (k=0), devolviendo {result}")

    return result


print("Recursion Example Results:")
tri_recursion_print(6)
