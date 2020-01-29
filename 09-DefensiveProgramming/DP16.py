from random import randint

x = randint(1,6)
print(x)
assert x in range(1,7), "Chyba uszkodzona kostka"
print(x)
