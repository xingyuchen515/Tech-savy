import math


# weight = input('What is your weight in lbs?')
# height = input('What is your height in inches?')**2
# weight = float(weight)
# height = float(height)
#
# BMI = 703 * weight / (height * height)
#
# if BMI >= 30:
#     print('You are in obesity.')
# elif 25 <= BMI <= 29.9:
#     print('You are overweight.')
# elif 18.5 <= BMI <= 24.9:
#     print('You are normal weight.')
# else:
#     print('You are underweight.')

# def calculate_bmi(weight, height):
#     bmi = 703 * weight / (height * height)
#     if bmi <= 18.5:
#         return "Your bmi is {:.1f}. You are underweighted.".format(bmi)
#     elif 18.5 < bmi <= 25:
#         return "Your bmi is {:.1f}. You are normal-weighted.".format(bmi)
#     elif 25 < bmi <30:
#         return "Your bmi is {:.1f}. You are overweighted.".format(bmi)
#     else:
#         return "Your bmi is {:1f}. You are in obesity.".format(bmi)
#
# weight = input('Enter your weight:')
# height = input('Enter your height:')
# weight = float(weight)
# height = float(height)
#
# print(calculate_bmi(weight, height))

# def countdown(n):
#     import time
#     time.sleep(1)
#
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
#
# countdown(5)
#
# def fab(n):
#     """
#     this function will return the nth Fabonacci number.
#
#     """
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fab(n-2) + fab(n-1)
#
# for i in range(1, 10):
#     print('The {}th Fabonacci number is {}.'.format(i, fab(i)))


# sum = 0
# for i in range(1, 11):
#     print('In the {}th iteration, current i*i is {}, sum is {}.'.format(i, i*i, sum))
#     sum = sum + i*i
#     print('\t after adding square of i, the new sum is {}\n'.format(sum))
#
# print(sum)

#Calculate the value of your name
total_value = 0
name = 'xingyu'

for letter in name:
    total_value = total_value + (ord(letter)-96)

print('The value of name {} is {}.'.format(name, total_value))

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        import time
        time.sleep(1)

    print('Blastoff!')

countdown(5)

result = 0
for number in range(1, 1001):

