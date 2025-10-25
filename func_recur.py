def hlo(name):
    print(f"hello {name}")

def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n
# name=input("Enter your name: ")
# # hlo(name)
n=int(input("Enter the number: "))
print(fact(n))

