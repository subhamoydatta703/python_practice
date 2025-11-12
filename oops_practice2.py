class Programmer:
    company="SoftwareCompany"
    def __init__(self, name, lan, sal):
        self.name= name
        self.lan = lan
        self.sal = sal
p1 = Programmer("Rahul", "Python", 2500000)
p2 = Programmer("Rohit", "Java", 2500000)
p3 = Programmer("Ronit", "Js", 1800000)
print(p1.company)
print(p2.lan)
print(p3.sal)