'''
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
'''

from math import *  #import modułu math
r = 5 #promień koła

p = pi * r**2 #pole koła
obw = 2 * pi * r #obwód koła

pole = ("Pole koła o promieniu {} wynosi {}")
obwód = ("Obwód koła o promieniu {} wynosi {}")

#rezultaty

print(pole.format(r, p))
print(obwód.format(r, obw))
