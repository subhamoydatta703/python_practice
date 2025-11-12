class Programmer:
    company="SoftwareCompany"
    def __init__(self, name, lan, sal):
        self.name= name
        self.lan = lan
        self.sal = sal


class Calculator:
    def __init__(self, num):
        self.num=num
    def sq(self):
        return self.num**2
    def cube(self):
        return self.num**3
    def roots(self):
        return round(self.num**0.5, 2)
    @staticmethod
    def greet():
        print("Hello")

p1 = Programmer("Rahul", "Python", 2500000)
p2 = Programmer("Rohit", "Java", 2500000)
p3 = Programmer("Ronit", "Js", 1800000)
# print(p1.company)
# print(p2.lan)
# print(p3.sal)

n = Calculator(5)
print(n.sq()) 
print(n.cube()) 
print(n.roots()) 
n.greet()
