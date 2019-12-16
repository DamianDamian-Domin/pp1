'''
program
'''
from random import *
def losowanie():
    liczba = randint(0, 50)
    return liczba

liczby = []
for a in range(0, 1000):
    liczby.append(losowanie())
    

p = 0
np = 0
for x in liczby:
    if x % 2 == 0:
        p += 1
    else:
        np +=1

p1 = p/len(liczby) * 100
np1 = np/len(liczby) * 100

print(f'Liczby parzyste w procentach: {p1:.2f}%\nLiczby nieparzyste w procentach {np1:.2f}%')            



    