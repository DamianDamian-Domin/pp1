'''
program
'''
y = 0
i = 1
l = 0
while i == 1:
    x = int(input("Wprowadź liczbę: "))
    y = x + y
    l += 1
    if x == 0:    
        break
print(f'Rezultat: Liczb = {l-1} Suma = {y} Średnia = {y/l}')