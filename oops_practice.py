# # student class to print avg marks

# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def avg(self):
#         a= sum(self.marks)/len(self.marks)
#         print(round(a, 2))
        


# s1 = Student("Rohit", [95,55,85])

# s1.avg()
        
# create account class with 2 attributes- balance and a/c no.
# create method for debit, credit and printing the balance

# class Account:
#     def __init__(self, bal, acc_no, ):
#         self.bal= bal
#         self.acc_no = acc_no
#     def credit(self, amount):
#         self.bal+=amount
#         print(f"{amount} credited and available balance is {self.bal}")
#     def debit(self, amount):
#         self.bal-=amount
#         print(f"{amount} debited and available balance is {self.bal}")
    
# acc = Account(10000, 12345)
# print(acc.bal)

# acc.credit(5000)
# print(acc.bal)

# acc.debit(2000)
# acc.debit(1000)

# print(acc.bal)


class Marks:
    def __init__(self, name, marks):
        self.name=name
        self.__marks=marks

    def getMarks(self):
        print(self.__marks)

    def setMarks(self, newmarks):
        self.__marks=newmarks
s1= Marks("Rohit", 55)

print(s1.name)
s1.getMarks()