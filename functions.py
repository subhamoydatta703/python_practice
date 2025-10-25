#function
def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

x=2
y=5
# print(sum(x, y))
# print(sub(x, y))

#recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
# print(fact(4))

#Using default arguments

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Subhamoy")

#keyword arguments

def hlo(name, age):
    print(f"Hello {name}, age is {age}")

hlo("sd", 25)