s1 = "Hello Java"


# List of String Methods
print(s1.endswith("Java"))
print(s1.startswith("Java"))
print(s1.find("llo"))  # searches first index of first match
print(s1.rfind("llo"))  # find but backwards
print(s1.count("o"))  # counts occurences
print(s1.capitalize())  # Only first letter of string
print(s1.lower())  # every letter lowercase
print(s1.upper())  # every letter uppercase
print(s1.title())  # every starting letter
print(s1.swapcase())  # swaps the cases for all letter
# every instance you see param1, replace w/ param2
print(s1.replace("ll", "xx"))
print(s1.lstrip())  # remove spaces from left side
print(s1.rstrip())  # remove spaces from right side
print(s1.strip("ll", "xx"))  # remove spaces from both sides
print(s1.center(20))  # make 20 spaces and put s1 in middle
print(s1.ljust(20))  # make 20 spaces and put s1 on left
print(s1.rjust(20))  # make 20 spaces and put s1 on right

print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
