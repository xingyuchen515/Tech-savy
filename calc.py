# a = 'ABC'
# b = 'XYZ'
#
# print('a is', a, ', b is', b)
#
# first_name = 'john'
# last_name = 'Lennon'
# # print = (first_name + " " + last_name)
#
# name = first_name + " " + last_name
#
# # print('hello,', name)

# print('hello, {}! You are {} years old.',format(name,20))

# template = 'hello, {}! You are {} years old.'
#
# name1 = 'Grace'
# age1 = 20
#
# name2 = 'Aida'
# age2 = 18
#
# print(template.format(name1, age1))
#
# print(template.format(name2, age2))
#
# print('Pi equals {:.2f}'.format(3.1415926))
#
# template = 'Hello, {name}! You are {age} years old.'
# print(template.format(age=age1, name=name1))
#
# import math
#
# print(math.pow(math.pi, 5))
# print(math.pi)
#
# 'Pi equals {:.2f}.'.format(3.1415926)
#
#
# print(2**38)
#
# print('1 + 2 + 3=', 1 + 2 +3)
#
# name = input()
#
# print('hello,', name)
#
# template = 'Hi, I am {}. I am {} years old!'
# name1 = 'Bobo'
# age1 = 12
#
# name2 = 'Xixi'
# age2 = 10
#
# print(template.format(name1, age1))
# print(template.format(name2, age2)

n = 2**70
print(n)

template = 'Hello, {}! You are {} years old!'
name1 = 'Bobo'
age1 = 12
name2 = 'Miaomiao'
age2 = 4
print(template.format(name1, age1))
print(template.format(name2, age2))

template = 'Hello {name}! You are {age} years old.'
print(template.format(name=name1, age=age1))

message = 'I did something cool today!'
n = 100
pi = 3.1415926
print(message)

print(2*3)

print(2**3)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

first_name = 'Yuan'
last_name = 'Wang'
print(first_name, last_name)

print(first_name + last_name)

print(first_name + " " + last_name)

print('lalalalal,hahahah'*8)

print('Hello, {}!'.format('world'))

print('Hello, this is {world}.'.format(world='nothing'))

print('Today is {Saturday}!'.format(Saturday='not saturday lol'))

print('Congratulations, {}, you won {:d}th Academy Award.'.format('La la Land', 89))


print('Pi equals {:.2f}.'.format(3.1415926))

print('Today is {:2d}-{:02d}.'.format(3, 5))

print('Growth rate: {:.2%}'.format(0.07))

minute = 45
percentage = (minute * 100 / 60)
print(percentage)


# sphere = ((4 / 3) * pi * radius**3)
# pi = 3.1415926
# radius = 5
# print(sphere)
#
# print('(4 / 3) * pi * {radius}**3'.format(radius =  5)

number_of_seconds_in_one_minute = 60

seconds = 42 * number_of_seconds_in_one_minute +42
print(seconds)

print('There are {} seconds.'.format(seconds))

number_of_kilograms_in_one_mile = 1.61
miles = 10 / number_of_kilograms_in_one_mile

print(miles)

print('There are {:.2f} miles.'.format(miles))

# Average_pace = miles / seconds
#
# number_of_seconds_in_one_hour = 60
#
# Average_speed = Average_pace * number_of_seconds_in_one_hour

# Pi = 3.1415926
# radius = 5
# Sphere = (4 / 3)* Pi* radius**3
# print('The volume of sphere is {:.2}'.format(Sphere)


# COVER_PRICE_PER_BOOK = 24.95
# DISCOUNT = 0.4
# NUMBER_OF_BOOKS = 60
# WHOLESALE_COST = COVER_PRICE_PER_BOOK * DISCOUNT + (NUMBER_OF_BOOKS-1) * 0.75 + 1 * 3
# print(WHOLESALE_COST)

# Exercise 1.1

import math
r = 5
volume = (4/3)*math.pi*math.pow(r, 3)
# volume = (4/3)*math.pi*(r**3)
print('The volume of a sphere of {} is {:.3f}.'.format(r, volume))

r = input("Please enter a number:")
print(type(r))

r = float(r)
print('After conversion,', type(r))
volume = (4/3)*math.pi*math.pow(r, 3)
print('The volume of a sphere of {} is {:.3f}.'.format(r, volume))

# Exercise 1.3

hour = 3
minutes = 2

print('Current time is {:02}:{:02}.'.format(hour, minutes))

print(1+2)

import datetime
print(datetime.datetime.now())
print(now)
print(now.hour, now.minute, now.second)
print(now.year)

