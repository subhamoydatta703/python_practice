from functools import reduce

# lambda function 

sqr = lambda x: x**2
print(sqr(5))

#.join()

a = ["Rahul", "Rohan", "Ronit"]
# print("-".join(a))

# map(), filter(), reduce()

lst = [1, 2, 3, 4]
list_square = lambda x:x**2
lst_sqr=list(map(list_square, lst))
print(lst_sqr) #gives a new list with squared values of each elements of lst

list_even = lambda x: x%2==0
evens = list(filter(list_even, lst))
# print(evens)

def sum(a, b):
    return a+b
print(reduce(sum, lst))

# working of reduce() ->
# lst = [1, 2, 3, 4] 
# dry run->
# 1+2=3 then 3+3=6 then 6+4=10
#final output of reduce() -> 10



