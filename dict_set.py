#dictionary
std={
    "name": "Subhamoy",
    "age": 25,
    "sub":"cse"
}
print(std["age"])
print(list(std))
std["clg"]="bwu"
print(std)
del std["age"]
print(std)

for key, value in std.items():
    print(key, ":", value)

print(std.get("name"))

std["clg"]="iit"
print(std)

print(std.keys())
print(std.values())

#sets

set1= set()
set1.add(1)
set1.add("python")
set1.add("bwu")
set1.add(10)
print(set1)
set1.remove(10)
print(set1)
set2={1,3,5,10}
# set1.update(set2)
# print(set1)
print(set1.union(set2))
# print(set1)
# set2.add(15)
a={1,2,3,4}
b={3,4,5,6}
# print(set1)
print(a.intersection(b))
