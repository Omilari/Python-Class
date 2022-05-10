
# List Methods
# .append: appends one element to the end of the list
# .insert: inserts at a specific index and shift everything to the right (previous index 2 becomes index 3)
# .remove: removes the first element from the list
# index: finds the first index of a number
#   with the index method you can add a starting point paramters that will start indexing at the specified point
#   i.e. list.index(70, 4)
#   if it doesn't find anything it "blows up"
# .count: counts the numbers of elements
# .sort: sorts the numbers
# You can use the "reverse" parameter to sort in reversed order
# .reverse: reverses the list
# .extend: extends list with another list
# .pop #remove element at specific index and return to the numbers, if no specifications it pops the last element


# functions you can use of lists
# len(list) #returns the number of elements in a list
# max(list) #returns the largest element in a list
# min(list) #returns the smallest element in a list
# sum(list) #returns the sum of the elements in a list
# random.shuffle(list1) #Shuffle the items in the list

# You can concatenate lists via "+" i.e: list3 = list1 + list2
# you can multiple lists too via "*" i.e: list3 = 2 * list1
# [2:4] - 2, 3
# in: see if a number is in a list

# join is a string method
listCheck = "a b c d e f"
l1 = list(input("Put Number of Values: "))
# joins all the elemnts together in the list and when you do put an empty space between
" ".join(l1)

print(l1)


def sortStr(str):
    l1 = list(str)
    l1.sort()
    return "".join(l1)


print(sortStr("yessuh"))


def reverseStr(str1):
    return str1[::-1]


l1 = [2, 4, 7, 3]
l2 = []
for elem in l1:
    l2.append(elem * 2)

# List Comprehension
# can be written like...
l3 = [2 * x for x in l1]
l4 = [x for x in l1 if x < 6]
l6 = [x for x in l1 if x % 2 == 0]

print(l2)
print(l6)


# list comparisons compare the first different and which ever is true of the first instance is true of the list
l1 = [10, 5, 7, 100]
l2 = [10, 2, 9, 200, 1000]
print(l1 > l2)

# String Method .split() makes a list of string seperated by space "by default", can specify split parameter


def change(str1):
    str1 = "Python"


str1 = "Hello"
change(str1)
print(str1)

# Most Data Types are Immutable (unchangeable)
# Lists are Mutable
# i.e


def changeList(l2):
    l2[0] = 1000


l1 = [1, 2, 3]
changeList(l1)
print(l1)


# x is 1
# y is 5555
