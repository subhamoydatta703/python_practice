from collections import Counter 
import itertools
import statistics

# count the number of each character
# print(Counter("Subhamoy Datta  "))



# Combination: selecting items where order does not matter (e.g., AB = BA)
# print(list(itertools.combinations([7,8,9,10],3))) 


# Permutation: selecting items where order matters (e.g., AB ≠ BA)
# print(list(itertools.permutations([7,8,9,10],3))) 

#calculate mean value
print(statistics.mean([1,2,3,4]))

#calculate linear regression
x=[1,2,3,4,5]
y=[7,8,9,5,4]
print(statistics.linear_regression(x,y))

