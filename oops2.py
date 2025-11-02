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

r1 = BigRoom(35)
print(r1.doors)
print(r1.size)
print(r1.color)
        



