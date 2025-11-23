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
# print(statistics.mean([1,2,3,4]))

#calculate linear regression
def predict(x):
    prediction = (res.slope*x)+res.intercept
    if(prediction>=100):
        return 100
    else:
        return prediction

#based on hrs of study how much numbers you get
hrs=[1,2,3,4,5] 
marks=[50, 60, 70, 85, 95]
res=(statistics.linear_regression(hrs, marks))

print(predict(2.5))