# del keyword

# In Python OOP (Object-Oriented Programming), the del keyword is used to delete objects, object properties (attributes), or variables.

class Student:
    def __init__(self, name):
        self.name = name

s1= Student("Rahul")
# print(s1)
# print(s1.name)

# del s1

# print(s1)

# "__" before atribute_name -> the attribute becomes private(like): eg., __password

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    
    def Getpass(self):
        return self.__acc_pass
    
a1= Account(12345, 7890)

# When you use double underscore (__) before a variable name,
# Python performs name mangling — it internally changes the variable’s name to:

# _Account__acc_pass


# So __acc_pass becomes private and cannot be directly accessed from outside the class.
# print(a1.__acc_pass)
print(a1.Getpass()) # best way to get the private data(like passwords) here we use encapsulation
        



