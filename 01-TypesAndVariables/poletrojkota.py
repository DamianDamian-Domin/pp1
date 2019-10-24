'''
Obliczanie pola trójkąta
'''
from math import *

a = float(input('Wprowadź długość boku a')) #długość boku a
b = float(input('Wprowadź długość boku b')) #długość boku b
c = float(input('Wprowadź długość boku c')) #długość boku c
p = (a + b + c) * 1/2                       #połowa obwodu trójkąta

Pt = sqrt(p*(p-a)*(p-b)*(p-c))              #pole trójkąta

print("Pole trójkąta o długości boków a = {:.2f} b = {:.2f} c = {:.2f} wynosi {:.2f}".format(a, b, c, Pt))








