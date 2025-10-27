# student class to print avg marks

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def avg(self):
        a= sum(self.marks)/len(self.marks)
        print(round(a, 2))
        


s1 = Student("Rohit", [95,55,85])

s1.avg()
        