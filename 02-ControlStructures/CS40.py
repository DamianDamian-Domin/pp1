'''
program
'''

from random import *

jedynka = 0
dwójka = 0
trójka = 0
czwórka = 0
piątka = 0
szóstka = 0

for i in range(100):
    x = randint(1, 6)
    if x == 1:
        jedynka += 1
    elif x == 2:
        dwójka += 1
    elif x == 3:
        trójka += 1
    elif x == 4:
        czwórka += 1
    elif x == 5:
        piątka += 1
    else:
        szóstka += 1  

print(f'jedynka = {jedynka}\ndwójka = {dwójka}\ntrójka = {trójka}\nczwórka = {czwórka}\npiątka = {piątka}\nszóstka = {szóstka}')          
            

