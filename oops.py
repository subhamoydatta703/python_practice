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

class Person:
    def __init__(self, name):
        self.name = name

    def sound(self):  # 'self' here refers to the same object that was created using __init__()
        print(self.name,"talk....")
p1= Person("Rahul")
p1.sound()
print(p1.name)

class Person:
    species = "Human"   # Class attribute

    def __init__(self, name):
        self.name = name  # Object attribute

# Create two objects
p1 = Person("Subhamoy")


print(p1.name)      # Object attribute -> unique for p1
print(p1.species)   # Class attribute -> same for everyone

# priority= object attribute > class attribute
