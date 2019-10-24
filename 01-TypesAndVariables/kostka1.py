'''
Program do losowania kostką
'''

from random import *

x = randint(1, 6) #rzut pierwszy
y = randint(1, 6) #rzut drugi
z = randint(1, 6) #rzut trzeci
suma = x + y + z

#rezultat

print("Pierwszy rzut kostką wyniósł {} drugi wyniósł {} trzeci wyniósł {}".format(x, y, z))
print("Suma oczek z trzech rzutów wyniosła {}".format(suma))
