'''
program
'''

from classes import konto

k1 = konto(input("Wprowadź numer rachunku: "))

k1.stan()
k1.wpłata(25.30)
k1.stan()
k1.wypłata(31.70)
k1.stan()
k1.wypłata(14)
k1.stan()
