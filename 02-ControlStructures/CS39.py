'''
program
'''

x = 0
y = 1

for i in range(0, 25):
    print(f'{x} {y}',end=" ")
    x = x + y
    y = y + x
