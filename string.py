team = 'New England Patriots'
#
# print(len(team))
#
# letter = team[1]
# print(letter)  #n is the 0 character, e is 1
#
# print(team[0]) #must be integer
#
# print(team[19])
#
# print(team[len(team)-1])
# #=
# print(team[-1])
#
# print(team[-20])  #= team(1)

# for letter in team:
#     print(letter)
#
#
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     # if letter == 'O' or letter == 'Q':
#     if letter in 'OQ':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)



print(team[0:11])  #0 to the number before 11
#is the same as
print(team[:11])

print(team[12:20])   #12 to number 19
#is the same as
print(team[12:])

print(team[:])  #it's the whole!

print(team[::2])  #Every other letter

print(team[::-1])   #Backwards

name = 'xingyu'

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome(name))


word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'aeoiuAEOIU':
        count = count + 1
print(count)

name = 'Anna'
new_name = name[:2]+name[-1] #first two letters + last letter
print(new_name)

new_team = ""
for letter in team:
    if letter != 'a':
        new_team = new_team+letter

print(new_team)

print(team.upper())

print(team.find('w'))  #the position is 2


