# Chapter03: 7,9,11,14
import random

# Question 7
cash = float(input('Enter in cash Amount: '))

hundreds = cash // 100
cash %= 100
tens = cash // 10
cash %= 10
dollars = cash // 1
cash %= 1
quarters = cash // .25
cash %= .25
dime = cash // .10
cash %= .1
nickel = cash // .05
cash %= .05
penny = cash // .01
cash %= .01

print('Your total is broken down to:')
print(str(hundreds) + ' hundreds')
print(str(tens) + ' tens')
print(str(dollars) + ' dollars')
print(str(quarters) + ' quarters')
print(str(dime) + ' dimes')
print(str(nickel) + ' nickels')
print(str(penny) + ' pennies')


# Question 9
weight1, package1 = eval(input(
    'Enter the Weight and then the Price for Package 1 (i.e: weight, price): '))
weight2, package2 = eval(input(
    'Enter the Weight and then the Price for Package 2 (i.e: weight, price): '))

if package1 < package2:
    print(package1)
elif package1 > package2:
    print(package2)
else:
    print('they both work!!')

combpack1 = package1 / weight1
combpack2 = package2 / weight2
# print('package1: ' + str(combpack1) + 'package2: ' + str(combpack2))
if combpack1 < combpack2:
    print(package1)
elif combpack1 > combpack2:
    print(package2)
else:
    print('they both work!!')


# Question 11
monthz = int(input('Enter a month in the year (e.g., 1 for Jan):'))
year = int(input('Enter a year: '))

isLeapYear = bool((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))


# index + 1
monthzs = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
           'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
inc = 0
while inc < len(monthzs):
    if(monthz == (monthzs.index('jan') + 1) or monthz == (monthzs.index('mar') + 1) or monthz == (monthzs.index('may') + 1) or monthz == (monthzs.index('jul') + 1) or monthz == (monthzs.index('aug') + 1) or monthz == (monthzs.index('oct') + 1) or monthz == (monthzs.index('dec') + 1)):
        print(monthzs[inc + 1] + ' ' + str(year) + ' has 31 days')
        break
    elif(monthz == (monthzs.index('apr') + 1) or monthz == (monthzs.index('jun') + 1) or monthz == (monthzs.index('sep') + 1) or monthz == (monthzs.index('nov') + 1)):
        print(monthzs[inc + 1] + ' ' + str(year) + ' has 30 days')
        break
    elif(monthz == (monthzs.index('feb') + 1) and isLeapYear == True):
        print(monthzs[inc + 1] + ' ' + str(year) + ' has 29 days')
        break
    else:
        print(monthzs[inc + 1] + ' ' + str(year) + ' has 28 days')
        break

# set mon to something / print something
# 31 = jan, mar, may, jul, aug, oct, dec
# 30 = apr, jun, sep, nov
# 28 = feb isLeapYear = false
# 29 = feb isLeapYear = true

# Question 14

flip_value = random.randint(0, 1)
guess = int(input("Enter 0 for head and 1 for tail: "))

coin = ['heads', 'tails']
if (guess == flip_value):
    print('congrats it is ' + coin[guess])
else:
    print('Sorry, it is ' + coin[flip_value])
