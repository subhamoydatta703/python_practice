# del keyword

# In Python OOP (Object-Oriented Programming), the del keyword is used to delete objects, object properties (attributes), or variables.

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1= Student("Rahul")
# print(s1)
# print(s1.name)

# del s1

# print(s1)

# "__" before atribute_name -> the attribute becomes private(like): eg., __password

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
    
#     def Getpass(self):
#         return self.__acc_pass
    
# a1= Account(12345, 7890)

# When you use double underscore (__) before a variable name,
# Python performs name mangling — it internally changes the variable’s name to:

# _Account__acc_pass


# So __acc_pass becomes private and cannot be directly accessed from outside the class.
# print(a1.__acc_pass)
# print(a1.Getpass()) # best way to get the private data(like passwords) here we use encapsulation
        
# class Student:
#     def __init__(self, name):
#         self.name = name

#     # convert methods into private -> the internal functions of this class can access this private method
#     def __Greet(self):
#         print("Hello")

#     def Wlc(self):
#         self.__Greet()

# s1= Student("Rahul")

# # print(s1.__Greet())
# s1.Wlc() 

# inheritance -> inherit the properties from parent class to child class

# syntax -> another_class another_class_name(parent_class):

class House:
    def __init__(self):
        self.windows = True
        self.doors = True

class Building(House):
    # def __init__(self, room):
    def __init__(self):
        # super().__init__() → calls House.__init__() → sets windows=True, doors=True
        super().__init__()  # call House constructor
        self.color= "blue"
        
        
class BigRoom(Building):
    # def __init__(self,room, size):
    def __init__(self, size):
        super().__init__()
        self.size=size
# b1 = Building()

# print(b1.doors)
# print(b1.color)

# r1 = BigRoom(35)
# print(r1.doors)
# print(r1.size)
# print(r1.color)
        
# Multiple inheritance -> one child class got more than one parent class's properties

# class Father:
#     def skills(self):
#         print("Can drive and repair things")

# class Mother:
#     def skills(self):
#         print("Can cook and paint")

# # Child inherits from BOTH Father and Mother
# class Child(Father, Mother):
#     def skills(self):
#         # call both parents’ versions
#         Father.skills(self)
#         Mother.skills(self)
#         print("Also good at coding!")

# c = Child()
# c.skills()


# sometimes we want a method that works for the whole class, not just one object.
# For that, we use @classmethod.
# @classmethod -> It can access and modify class-level variables, but not instance variables directly.

# Syntax
# class ClassName:
#     @classmethod
#     def method_name(cls, args):
#         

class Student:
    school_name = "Brainware University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


# Creating objects
s1 = Student("Subhamoy")

print(s1.school_name)   # Brainware University

# Changing class variable using classmethod
Student.change_school("IIT Madras Online BS")

# Student.change_school("IIT Madras Online BS")

# Here’s what’s happening:

# Student → means we are calling the method using the class, not an object.

# .change_school → this is the method we want to run.

# "IIT Madras Online BS" → this is the new name we are passing to the method.

print(s1.school_name) 




