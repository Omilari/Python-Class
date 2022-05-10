# Tuples
# like a list but can never change non-immutable
t1 = (1, 4, 2, 6)

print(len(t1))  # min, max, sum, etc...

if 4 in t1:
    print("Hello")

# tuple "easier to maintain unchangeable variables"
t2 = tuple("abcde")

# conversion, tuple to list, then list to tuple
t3 = tuple([1, 2, 3, 4])
l1 = list(t3)

# get first index the same as lists
print(t1[3])


# Sets
# - don't have any order
# - can't have duplicates in a set

s1 = {}  # empty set
s2 = {1, 5, 3}
s3 = set({5, 8, 7})
s4 = set([1, 4, 3, 2])
s6 = set("abcdda")

# no indexes in sets
# can't convert set back to a list b/c order is not mentioned

# subset, superset
s1 = {1, 2}
s2 = {3, 2, 1}

print(s2.issuperset(s1))  # s2 is a superset of s1
print(s1.issubset(s2))  # s1 is a subset of s2

# Union, Intersection, Subtraction, Symmetric Diff
# union : what is in A, B, and Both
s3 = s1 | s2
s4 = s1.union(s2)

# intersection: what is in both A and B
s5 = s1 & s2
s6 = s1.intersection(s2)

# subtraction: A (minus) any common items w/ B
s7 = s1 - s2
s8 = s1.difference(s2)

# A ^ B (symmetric difference): Everything except what A and B hold in common
s9 = s1 ^ s2
s10 = s1.symmetric_difference(s2)


# Comparing Sets
# < > : subset, superset
# == : equivalence

# add to set
s1.add(100)

# remove from set
s1.remove(100)

# Sets are faster than lists


# Dictionary
d1 = {}  # empty set or dictionary
d2 = {123: "Hello"}  # query values based on key
# keys should be unique
# valubes can be duplicates
#   Hashmap is the same in Java
print(d2[123])  # keys can be any type and any value as long as it is unique

d2[987] = "Java"  # adds another key : value pair from dictionary
d2[888] = "Yessuh"
d2[324] = "YKWWD"
print(d2[987])

# Sidenote: In dictionaries order is important

print(len(d2))

del d2[123]  # deletes a key : value pair from dictionary
d2[123] = "Hello"

# For Loop
for keyss in d2:
    print("key:", keyss, end=" ")
    print("value:", d2[keyss])

# In
if 888 in d2:
    print("Free DDawg")


# Methods
# gets the keys and puts it in a list... note always put it in a list
print(list(d2.keys()))
print(list(d2.values()))  # gets the values in dictionary and puts it in a lsit
# get the key value pairs and put them in a tuple, creates list of tuples
print(list(d2.items()))
# d2.clear()  # clears all items
# this is safe, meaning if the key is not there it won't crash, "gets the key associated with value"
print(d2.get(123))
print(d2.popitem())
print(d2.pop(123))


# When reading a file, every element in the list is one line, and every line is a string
