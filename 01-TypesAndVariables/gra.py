'''
program do gry z komputerem
'''

from random import *

x = randint(1, 6) #rzut kostką komputera

y = int(input("wprowadź liczbę od 1 do 6")) #próba zgadnięcia przez gracza

if x==y:
    print("true")
else:
    print("false")