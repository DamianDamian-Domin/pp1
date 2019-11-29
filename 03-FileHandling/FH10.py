'''
program
'''
s = 0
with open('numbers.txt') as file:
    for x in file:
        s = s + int(x)
print(s)