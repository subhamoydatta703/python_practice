# Walrus operator(:= )

# if(val:=int(input("enter a number: "))>5):
#     print("grater than 5")

# type definition/alias(Using  : symbol after the variable and then write the data type)


n: int = 5
x: str = "Rahul"

def sum(x: int, y: int) -> int:
    return x+y

print(sum(5,6))