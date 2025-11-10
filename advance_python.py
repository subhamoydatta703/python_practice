from typing import List, Tuple, Dict, Union


# Walrus operator(:= )

# if(val:=int(input("enter a number: "))>5):
#     print("grater than 5")

# type hints(Using  : symbol after the variable and then write the data type)


# n: int = 5
# x: str = "Rahul"

# def sum(x: int, y: int) -> int:
#     return x+y

# print(sum(5,6))

# Type definition/alias

type vector = list[float]


def scale(s: float, v:vector)->vector:
    return [s*num for num in v]

v1: vector = [1.0, 2.0, 3.0]
print(scale(2.0, v1))

# using typing module(advanced type hinting)

# Type Aliases (Type Definitions)
Vector = List[float]           # list of floats
UserData = Tuple[int, str]     # tuple: (id, name)
Marks = Dict[str, int]         # dictionary: name → marks
Number = Union[int, float]     # can be int or float 


# Assigning values using those types
v1: Vector = [1.2, 3.4, 5.6]
v2: Vector = [2.0, 4.0, 6.0]

user1: UserData = (101, "Subhamoy")
user2: UserData = (102, "Rahul")

marks: Marks = {"Subhamoy": 95, "Rahul": 88, "Ankit": 76}

# Union means a variable or function can accept more than one type of value, but at any one moment, it can hold only one type of value.
x: Number = 10
y: Number = 5.5

# Using and printing them
print("Vector 1:", v1)
print("Vector 2:", v2)
print("User 1:", user1)
print("User 2:", user2)
print("Marks:", marks)
print("x + y =", x + y)