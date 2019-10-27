'''
program
'''

from math import *

a = int(input("Wprowadź wartość a: "))
b = int(input("Wprowadź wartość b: "))
c = int(input("Wprowadź wartość c: "))

delta = b**2 - 4*a*c
x1 = 0
x2 = 0
x0 = 0

if delta > 0:
    x1 = (-b - sqrt(delta))/2 * a
    x2 = (-b + sqrt(delta))/2 * a
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
elif delta == 0:
    x0 = (-b/2 * a)
    print(f'x0 = {x0}')
else:
    print("Brak pierwiastków")       
