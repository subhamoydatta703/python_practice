# marks=[10,20,30,40,50]
# print(marks[1:4:2]) # list slicing: list_nme[start:end:steps]
# List methods example

lst = [1, 2]

# append(): Add single item at end
lst.append(3)
print("append:", lst)

# extend(): Add multiple items
lst.extend([4, 5])
print("extend:", lst)

# insert(): Add item at specific index
lst.insert(2, 99)
print("insert:", lst)

# remove(): Remove first matching value
lst.remove(99)
print("remove:", lst)

# pop(): Remove and return last item
last = lst.pop()
print("pop (last item):", last, "| list:", lst)

# clear(): Remove all items
temp = lst.copy()  # save a copy before clearing
temp.clear()
print("clear:", temp)

# index(): Get index of value
print("index of 3:", lst.index(3))

# count(): Count occurrences of value
# Create a list with repeated items
fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]

# Count how many times 'apple' appears
apple_count = fruits.count("apple")

# Count how many times 'banana' appears
banana_count = fruits.count("banana")

# Print the results
print("List:", fruits)
print("Apple count:", apple_count)     # Output: 3
print("Banana count:", banana_count)   # Output: 2
#extend in list to extend the list
lst.extend([2, 2])
print("count of 2:", lst.count(2))

# sort(): Sort the list
unsorted = [5, 3, 1, 4, 2]
unsorted.sort()
print("sort:", unsorted)

# reverse(): Reverse the list
unsorted.reverse()
print("reverse:", unsorted)

# copy(): Copy the list
copied = lst.copy()
print("copy:", copied)

# Create a tuple with repeated elements
numbers = (10, 20, 30, 20, 40, 20)

# Use count() to count how many times 20 appears
count_20 = numbers.count(20)

# Use index() to find the first index where 30 appears
index_30 = numbers.index(30)

# Output the results
print("Tuple:", numbers)
print("Count of 20:", count_20)     # Output: 3
print("Index of 30:", index_30)     # Output: 2
