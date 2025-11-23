from collections import Counter 
import itertools

# count the number of each character
print(Counter("Subhamoy Datta  "))



# Combination: selecting items where order does not matter (e.g., AB = BA)
print(list(itertools.combinations([7,8,9,10],3))) 


# Permutation: selecting items where order matters (e.g., AB ≠ BA)
print(list(itertools.permutations([7,8,9,10],3))) 


