# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# numbers = [42, 123]
# empty = []
#
# print(len(AFC_east))
#
# AFC_east_best = ['New England Patriots']
#
# print(len(AFC_east_best))
#
# #print(len(AFC_east_best))
#
# str_team = 'New England Patriots'
# #print(len(str_team))
#
# # print(str_steam(0))
# print(AFC_east[0])
# print('Miami Dolphins' in AFC_east)
#
# L = [
#         ['Apple', 'Google', 'Microsoft'],
#         ['Java', 'Python', ['Ruby', 'On Rail'], 'PHP'],
#         ['Adam', 'Bart', 'Lisa']
# ]
#
# #print(len(L))
# # print(L[0])
# print(len(L[1]))
#
# print(L[0][0])  #Apple
# print(len(L[0][0]))  #5
# print(L[1][2][0])  #Ruby
# print(L[1][2][1])  #On Rail
#
# AFC_east = ['New England Patriots',
#             'Buffalo Bills',
#             'Miami Dolphins',
#             'New York Jets']
#
# # print(AFC_east[2][5:])  # Dolphins
#
# for letter in AFC_east:
#     print(letter)
#
# for whatever in AFC_east:
#     print(whatever)
#
# AFC_west = ['Chargers', 'Raiders', 'Broncos', 'Chiefs']
#
# AFC = AFC_east + AFC_west
#
# print(AFC_east[1:3])  #Buffalo bills, Miami Dolphins
#
# print(AFC[1::2])  #Everyother
#
# print(AFC[1:4:2])   #Everythingother end before "Chargers"
#
# name = 'Maddison'
# t = list(name)
# # print(list(name))
#
# str_team = 'New England Patriots'
# t = str_team.split()
# # print(t)
#
# team_name = " ".join(t)
# print(team_name)

# del AFC[-2]
# print(AFC)

# del AFC[-2:]
# print(AFC)

# print(AFC_east)
#
# AFC_east[-1] = 'New York Giants'   #We replaced
# print(AFC_east)

# Dictionary

names = ['Bailey', 'Maddison', 'Aob']
scores = [60, 90, 100]

# grades = dict()
# or use
grades = {}
grades['Bailey'] = 60

# print(grades)

grades['Maddison'] = 90
grades['Aob'] = 100

print(grades)

print(grades['Maddison'])

grades['Aida'] = [99, 98]
print(grades)

# print(grades['Penny'])
print('Penny' in grades)

print(len(grades))
print()

for name in grades.keys():
    print(name)

for score in grades.values():
    print(score)

for item in grades.items():    #iteams is combination of keys and valuesz
    print(item)

