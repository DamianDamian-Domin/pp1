a = 5
b = 3

assert b!=0, "Dzielenie przez 0!"
assert type(a) == int and type(b) == int, "Licza musi być liczbą całkowitą!"

print(f'{a}/{b} = {a/b}')