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

class Human:
    def __init__(self, name):
        self.name=name

    @staticmethod
    def prop():
        print("Humans have hand, legs, face, etc.")

h1 = Human("Rohit")
print(h1.name)
h1.prop()