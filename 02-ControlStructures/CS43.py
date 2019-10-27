'''
program
'''

a = float(input('Podaj pierwszą liczbę: '))
b = float(input('Podaj drugą liczbę: '))
c = float(input('Podaj trzecią liczbę: '))
tablica = [a,b,c]
tablica.sort()
print(f'Liczby w kolejności rosnącej: {tablica}')