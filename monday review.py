# def print_twice(whatever_name):
#     print(whatever_name)
#     print(whatever_name)
# #
# print_twice('Babson')

import math
# def my_abs(whatever_number):
#     print(abs(whatever_number))
# print(my_abs(1))

# def give_me_a_break():
#     str1 = 'break'
#     return str1
#
# print(give_me_a_break())


# def give_me_a_break():
#     str1 = 'break'
#     return str1
#     print('another break')
#
# print(give_me_a_break())
#
# result = print_twice('Bing')
#
# print(result)
#
# import math
# def my_abs(a):
#     return abs(a)
# print(my_abs(-1))
#
# def move(x, y, step, angle):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)


# def quadratic(a, b, c):
#     x1 = (-b + math.sqrt(math.pow(b, 2) - 4*a*c)) / 2*a
#     x2 = (-b - math.sqrt(math.pow(b, 2) - 4*a*c)) / 2*a
#     return (x1, x2)
# print(quadratic(1, 2, 3))

# def quadratic(a, b, c):
#     discriminant = b**2 - 4 * a * c  # calculate the discriminant
# 
#     if discriminant >= 0:  # equation has solutions
#         x_1 = ((-b + math.sqrt(discriminant)) / 2 * a)
#         x_2 = ((-b - math.sqrt(discriminant)) / 2 * a)
#         return x_1, x_2
# 
#     else:
#         print('No Real Number Solution.')
#         return None
# 
# a = float(input('please enter a number:'))
# b = float(input('please enter a number:'))
# c = float(input('please enter a number:'))
# print('Results are:', quadratic(a, b, c))

# def square_plus_one(a, b):
#     return a * b + 1
# print(square_plus_one(1, 2))

# def quadratic(a, b, c):
#     x_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
#     x_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
#     return x_1, x_2
#
#
# print(quadratic(1, 2, 3))

# age = int(input('How old are you?'))
# if age >= 18:
#     print('You age is {}').format(age)
#     print('Adult')
# elif age >= 6:
#     print('You age is', age)
#     print('Teenager')
# else:
#     print('You age is', age)
#     print('Kid')

# if x == y:
#     print('x equals y')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')
import math

# def calculate_bmi(weight, height):
#     bmi = 703 * weight / (height * height)
#     if bmi < 18.5:
#         return 'Your bmi is {:.1f}. You are underweighted.'.format(bmi)
#     elif bmi < 25:
#         return 'You bmi is {:.1f}. You are normal weighted.'.format(bmi)
#     elif bmi < 30:
#         return 'You bmi is {:.1f}. You are overweighted.'.format(bmi)
#     else:
#         return 'You are in obesity.'.format(bmi)
#
# weight = input('Enter your weight:')
# height = input('Enter your height:')
# weight = float(weight)
# height = float(height)
#
# print(calculate_bmi(weight, height))

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
#
# print(countdown(3))

# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1)
#
# def recurse():
#     recurse()
#
# sum = 0
# for number in range(1, 1001):
#     print('in the {}th iteration, current number is {}, sum is {}'.format(number, number, sum))
#     sum = sum + number
#     print('\t after adding number, the new sum is {}\n'.format(sum))
#
# print(sum)

total_sum = 0
for i in range(1, 101):
    total_sum += i
print(total_sum)

total2 = 0
for i in range(1, 101):
    if i % 2 == 1:
        total2 += i
print(total2)

given_list = [5, 3, 1, -1, -3]
total3 = 0
j = 0
while j < len(given_list) and given_list[j] > 0:
    total3 += given_list[j]
    j += 1
print(total3)

total4 = 0
for i in given_list:
    if i <= 0:
        break
    total4 += i
print(total4)

word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count = count +1
print(count)

index = word.find('a')
print(index)

print(word.find('a', 10))




