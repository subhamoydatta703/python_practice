num1= float(input("Enter the first number: "))
op=input("Enter the operator(+, -, *, /): ")
num2=float(input("Enter the second number: "))
if(op!='+' or op!='+' or op!='+' or op!='+'):
    print("Invalid")
if(op=='+'):
    print("The sum is: ", num1+num2)
if(op=='-'):
    print("The minus is: ", num1-num2)
if(op=='*'):
    print("The multiply is: ", num1*num2)
if(op=='/'):
    print("The division is: ", num1/num2)