'''
program
'''

import re
with open('land.txt') as file:
    temp = re.findall('\d', file.read())
temp = [int(i) for i in temp]
print(sum(temp))