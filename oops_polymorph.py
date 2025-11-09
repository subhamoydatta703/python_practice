class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img= img
    def showNum(self):
        print(self.real, "i +", self.img, "j")
        # using dunder functions
    def __add__(self, num2):
        newNum1 = self.real + num2.real
        newNum2 = self.img + num2.img
        return Complex(newNum1, newNum2)
    def __sub__(self, num2):
        newNum1 = self.real - num2.real
        newNum2 = self.img - num2.img
        return Complex(newNum1, newNum2)

num1 = Complex(1, 4)
num2 = Complex(5, 6)
# num3=num1.add(num2)
# num3= num1+num2
num3= num1-num2
num3.showNum()