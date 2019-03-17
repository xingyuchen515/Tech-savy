#Exercise 0.2.1
NUMBER_OF_SECONDS_IN_ONE_MINUTE = 60
seconds = 42 * NUMBER_OF_SECONDS_IN_ONE_MINUTE + 42
print('There are {} seconds.'.format(seconds))

#Exercise 0.2.2
NUMBER_OF_KILOMETERS_IN_ONE_MILE = 1.61
miles = 10/NUMBER_OF_KILOMETERS_IN_ONE_MILE
print('There are {:.2f} kilometers in one mile.'.format(miles))

#hello.py
template = 'Hello, this is {}. I am {} years old.'
name1 = 'yuan'
age1 = 18

name2 = 'you'
age2 = 22

print(template.format(name1, age1))
print(template.format(name2, age2))

Pi = 3.1415926
print('Pi equals {:.2f}.'.format(Pi))

import math
print(math.pi)
print(math.pow(2, 3))

#Exercise 1.1
r = 5
volume = (4/3)*(math.pi)*(math.pow(r, 3))
print('The volume of the sphere of {} is {:.3f}.'.format(r, volume))

#Exercise 1.2
COVERPRICE_PER_BOOK = 24.95
DISCOUNT = 0.4
COVERPRICE = COVERPRICE_PER_BOOK * DISCOUNT
SHIPPING_COST_PER_BOOK = 0.75
SHIPPING_COST_FIRST_COPY = 3
WHOLESALE_BOOK = COVERPRICE*60 + 59 * SHIPPING_COST_PER_BOOK + 1 * SHIPPING_COST_FIRST_COPY
print(WHOLESALE_BOOK)

#Exercise 1.4
PERCENTAGE_OF_INCREASE = (89-82)/82
print('The percentage of increase is {:.2%}.'.format(PERCENTAGE_OF_INCREASE))

#Chapter2.py
print(len(str(2*1000000)))

import random
print(random.random())
random.choice([1, 2, 3, 4, 5])

print(random.random())
random.choice([10, 20, 30, 40, 50])

print(len('Jkdjskldfj'))

print(math.sqrt(25))

print(int(random.random()*100))

print(int(random.random()*50))

print(int(random.random()*2000000))

print(random.randint(1, 6))

print(random.randint(10, 25))

print(random.randint(20, 23))

print(random.choice([4, 2, 7, 14]))

print(random.choice(['red', 'green', 'blue']))

print(random.choice(['gift', 'present', 'nothing']))

# lower = int(input('Please enter a number as lower bound:'))
# upper = int(input('Please enter a number as upper bound:'))
# print(random.randint(lower, upper))
#
# lower = int(input('Please enter a number as lower:'))
# upper = int(input('Please enter a number as upper:'))
# print(random.randint(lower, upper))

print("I'm saying \"OK\".")
print('I\'m learning \n\n python')
print('I\'m doing \n "homework".')

print('\\\n\\')

print('\\\t\\')
print(r'\\\t\\')

print('''line 1
...line 2
...line 3''')

print(3 > 2 and 3 > 5)
print(3 > 2 or 3 > 5)
print(3 > 2 or 3 > 5 or False or 100 < 100)
#
# age = int(input('How old are you?'))
#
# is_in_US = True
#
# answer = input('Are you in US?')
#
# if answer == 'no':
#     is_in_US = False
# if age < 21 and is_in_US:
#     print('Sorry, you cannot.')
# else:
#     print('Yes, you can.')

# age = int(input('How old are you?'))
# answer = input('Are you in US?')
#
# if age < 21 and answer == 'yes':
#     print('Sorry you cannot.')
# else:
#     print('Yes you can.')

# month = int(input('When is your birthday month?'))
# answer = input('Who is your favorate singer?')
#
# if month == 5 and answer == 'wangyuan':
#     print('Go marry him.')
# else:
#     print('He is not yours.')

name = input('What is your name?')
love = input('Who is your favorate singer?')

if name == 'xingyu' or love == 'wangyuan':
    print('Hello xingyu!')
else:
    print('Sorry I do not know you.')

