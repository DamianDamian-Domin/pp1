wiek = -5
if type(wiek) != int:
    raise TypeError('Wiek powinien byc liczbą całkowitą!')
elif wiek not in range(0, 120):
    raise ValueError('Wiek nieprawdziwy')
print(f'Masz {wiek} lat')