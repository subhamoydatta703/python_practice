# creating class:
# class Student:
#     name = "Subhamoy"

# creating object/instance of the class Student
# s1= Student()

# print(s1.name) # printing the name ofthe object

# init function =  constructor
#A constructor gives the object its initial data when it is created.
# In Python:

# The constructor is named __init__().

# It runs automatically whenever you create an object of the class.

# It helps to assign values to object attributes.

# Means → when you create an object, the constructor gives it its starting data (values) automatically.

# # Example in Python
# class Student:
#     def __init__(self, name, roll):
#         self.name = name       # setting the value of name for the object
#         self.roll = roll       # setting the value of roll for the object
#                                # In Python, self refers to the current object of the class.

# # create two objects
# s1 = Student("Subhamoy", 24) # You don’t write self when creating an object because Python adds it automatically behind the scenes.
# # print(s1.name, s1.roll)

# When you make a student object, the constructor gives it a name and roll number right away —
# you don’t have to assign them later manually.

# class Person:
    # def __init__(self, name):
        # self.name = name
# Here sound() is a method that belongs to this object
#methods are the functions that were written inside a class
    # def sound(self):  # 'self' here refers to the same object that was created using __init__()
#         print(self.name,"talk....")
# p1= Person("Rahul")
# p1.sound()
# print(p1.name)

# class Person:
#     species = "Human"   # Class attribute

#     def __init__(self, name):
#         self.name = name  # Object attribute

# # Create two objects
# p1 = Person("Subhamoy")


# print(p1.name)      # Object attribute -> unique for p1
# print(p1.species)   # Class attribute -> same for everyone

# priority= object attribute > class attribute

# class Student:
#     def __init__(self, name):   # this is a method (constructor)
#         self.name = name

#     def greet(self):            # this is also a method
#         print("Hello,", self.name)

# # creating an object of the class
# s1 = Student("Subhamoy")

# # calling the method
# s1.greet()

# def greet(self): → is a method (a function inside the class).

# self refers to the current object (s1 here).

# When we call s1.greet(), it prints Hello, Subhamoy.

# static method:

# A static method is a method inside a class that does not use self (object) or cls (class).
# It behaves like a normal function, but is logically grouped inside the class because it’s related to it.

# So —
# It cannot access or modify class or instance variables.
# It belongs to the class, not to any object.

# Syntax:
# class ClassName:
#     @staticmethod
#     def method_name():

# class Human:
#     def __init__(self, name):
#         self.name=name

#     @staticmethod #@staticmethod is a decorator
#     def prop():
#         print("Humans have hand, legs, face, etc.")

# h1 = Human("Rohit")
# print(h1.name)
# h1.prop()

# A decorator is a special function that adds extra features to another function or method —
# without changing its actual code.

# Example (simple view)

# Suppose you have a normal function:

# def greet():
#     print("Hello!")


# Now you want to add something extra, like a message before and after it.
# You can do it using a decorator.

# Basic Decorator Example:
# def decorator_func(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper

# @decorator_func
# def greet():
#     print("Hello!")

# greet()


# Output:

# Before the function runs
# Hello!
# After the function runs


# @decorator_func means → greet = decorator_func(greet)

# So the decorator wraps the greet() function and adds new behavior before and after it.

# In OOP:

# Decorators like @staticmethod or @classmethod are built-in decorators that change how a method behaves:

# @staticmethod → makes a method independent of object (self)

# @classmethod → passes cls (class) instead of self

# Decorator

# def decorator_func(func):     # func = greet
#     def wrapper():            # wrapper is a NEW function
#         print("Start")        # runs first
#         func()                # runs the real greet()
#         print("End")          # runs last
#     return wrapper            # send wrapper back

# @decorator_func
# def greet():
#     print("Hello!")

# greet()

# How it works

# When we write:

# def decorator_func(func):


# 👉 that func is a parameter — it will receive the function you decorate.

# So if you write:

# @decorator_func
# def greet():
#     print("Hello!")


# Then behind the scenes, Python does this:

# greet = decorator_func(greet)


# That means:

# func → becomes greet

# So inside the decorator, func() → actually means greet()

# Abstraction

# class  Car:
#     def __init__(self):
#         self.acc=False
#         self.clutch = False
#     def start(self):
#         self.acc=True
#         self.clutch= True
#         print("Car started...")

# c1 = Car()
# c1.start()

# When we call c1.start(), we only see the important action — “Car started...”.
# We don’t see the internal details like how self.acc and self.clutch became True.

# This is called abstraction — hiding unnecessary details and showing only the essential part.

#Encapsulation

class Account:
    def __init__(self, bal, acc_no, ):
        self._bal= bal
        self.acc_no = acc_no
    def credit(self, amount):
        self._bal+=amount
        print(f"{amount} credited and available balance is {self._bal}")
    def debit(self, amount):
        self._bal-=amount
        print(f"{amount} debited")
        print(f"Available balance is {self.get_bal()}")

    def get_bal(self):
        return self._bal
    
acc = Account(10000, 12345)
# print(acc.bal)

# acc.credit(5000)
# print(acc.bal)

# acc.debit(2000)
acc.debit(1000)
print(acc.get_bal())
# print(acc.bal)
