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

