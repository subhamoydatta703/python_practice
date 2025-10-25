#function
def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

x=2
y=5
# print(sum(x, y))
# print(sub(x, y))

#recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
# print(fact(4))

#Using default arguments

def greet(name="Guest"):
    print("Hello", name)

# greet()
# greet("Subhamoy")

#keyword arguments

def hlo(name, age):
    print(f"Hello {name}, age is {age}")

# hlo("sd", 25)

# Arbitrary Arguments

# When you don’t know how many arguments will be passed:

# *args → tuple of positional arguments

# **kwargs → dictionary of keyword arguments

# *args → for positional arguments (values without names)
# **kwargs → for keyword arguments (key=value pairs)

def show_args(*args):
    print(args)

# show_args(1,3,7,9, "Subhamoy", "Java")

def show_kwargs(**kwargs):
    print(kwargs)

# show_kwargs(name= "Subhamoy", age= 25, Course= "ai ml")

# global vs local scope

x = 10  # global

def func():
    x = 5  # local
    print("Inside:", x)

# func()
# print("Outside:", x)

# modify global scope

x=20
# print("Before modification, value of x is:", x)
def change():
    global x
    x=5
    print("Modified value of x:", x)

# change()

# printing list using function

# method 1:

def show_list(lst):
    print(lst)

my_list = [1, 2, 3]
show_list(my_list)

# method 2:

def show_items(*args):
    print(args)

my_list = [1, 2, 3]
show_items(my_list)





