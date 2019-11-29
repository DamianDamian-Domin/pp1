'''
program
'''
x = 0
with open('NoEducation.txt') as file:
    for line in file:
        x = x + 1
        print(x, line, end="")