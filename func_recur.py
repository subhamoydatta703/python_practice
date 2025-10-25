def hlo(name):
    print(f"hello {name}")

# def fact(n):
#     if(n==0 or n==1):
        # return 1
    # return fact(n-1)*n
# name=input("Enter your name: ")
# # hlo(name)
# n=int(input("Enter the number: "))
# print(fact(n))

# practice 

# length of a list
def length(my_list):
    return len(my_list)

# lst = [1,2,3,"subhamoy", 5]

# print(length(lst))

# elements of a list in single line

def show_list(items):
    for item in items: 
        print(item, end=" ")

lst = [1,2,3,"subhamoy", 5]

# show_list(lst)

# factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

# print(fact(4))

def currConverter(val):
    INR= val * 87.82
    return round(INR, 2)

print(currConverter(6))