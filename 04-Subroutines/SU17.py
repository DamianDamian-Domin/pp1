'''
program
'''
from random import *
def kostka():
    oczka = []
    for y in range(3):
       x = randint(0, 6)
       oczka.append(x)
    suma = sum(oczka)   
    print(f'Wyrzucone oczka: {oczka}\nSuma oczek: {suma}')
kostka()    

    


