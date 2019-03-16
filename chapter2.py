# print(3.14e-2)
#
# # length_of_number = len(str(2**1000000))
# #
# # print(length_of_number)
#
#
# print(len('Maddison'))
#
# import math
#
# print(math.pi)
# print(math.sqrt(25))
#
# import random
# print(random.random()*100)
#
# print(int(random.random()*100)) # a random integer between 0 and 100
#
# print(random.randint(1, 6)) # a random number between 0 and 6
#
# print(random.choice(["wangyuan", "cheyinyou", "liwenhan"])) # a random name in my boyfriend list
#
# print(random.choice([6, 15, 5, 11]))
#
# lower = int(input("Please a number as the lower bound:")) #别忘了加括号 integer
# upper = int(input("another one as upper bound:"))
# print(random.randint(lower, upper))
#
# # Strings
# I'm "OK".
# print("I'm \"OK\".") #to make "OK" have 引号
#
# print("I'm learning\nPython.") #\n means adding one line. 多加几个就多加几行

## Boolean (T or F)

print(3>2)
print(3>5)

print(3>2 and 3>5) #False
print(3>2 or 3>5)  #True (One of them is true, it's true)
print(3>2 or 3>5 or False or 100<100)  #True+False+False=True

# n = int(input())
# # print(n>3) #True
#
# print(n>3) #如果没有上面那个前提条件，n is not defined.


age = int(input("How old are you?"))

if age >= 21:  #age>=21 is a boolean
    print('Yes, you can.')
else:
    print('Sorry, you cannot.')


is_in_US = True

if is_in_US:
    print('in US!')
else:
    print('not')