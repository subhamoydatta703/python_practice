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

# print(currConverter(6))

# sum of first n natural numbers

def sum(n):
    if n==0 or n==1:
        return n
    else:
        return n + sum(n-1)
    
# print(sum(5))

# sum of digits

def sumDigits(n):
    if n==0 or n==1:
        return n
    else:
        temp2=n%10
        n = n//10
        return temp2 + sumDigits(n)
# print(sumDigits(123))

# Fibonacci series

def fab(n):
    if n==0 or n==1:
        return n
    else:
        return fab(n-1)+fab(n-2)
    
# print(fab(3))

# reverse a string
def revStr(str1):
    print(str1[::-1])

# revStr("Python")
    
# Sum of elements at even indices of a list

def sumEvenIdx(items):
    sum =0
    for i in range(len(items)):
        if(i%2==0):
            sum = sum + items[i]
    print(sum)



# power
def pow(n, x):
    if( n==0 or n==1):
        return n
    elif(x==0):
        return 1
    else:
        return n * pow(n, x-1)
    
# print(pow(3, 3))

# recursion to print elements of a list

def elm(items, i):
    if(i==len(items)):
        return
    print(items[i], end=" ")
    elm(items, i+1)
    
lst =[1,2,3,4,5]

elm(lst, 0)
