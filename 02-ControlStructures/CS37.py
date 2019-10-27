'''
program
'''

x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
z = float(input("Podaj trzecią liczbę: "))

if x > y and x < z or x > z and x < y:
    print(f'Mediana wynosi {x}')
elif y > x and y < z or y < x and y > z:
    print(f'Mediana wynosi {y}')
elif z > x and z < y or z < x or z > y:
    print(f'Mediana wynosi {z}')

          
