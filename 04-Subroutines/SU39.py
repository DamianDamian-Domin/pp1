'''
program
'''

def zakres(x, y, z):
    if z > x and z < y:
        print("Podana liczba mieści się w przedziale")
    else:
        print("Podana liczba nie mieści się w przedziale")

liczba1 = int(input("Wprowadź wartość x przedziału (x;y): "))
liczba2 = int(input("Wprowadx wartość y przedziału (x;y): "))
liczba3 = int(input("Wprowadź wartość z do sprawdzenia: "))

zakres(liczba1, liczba2, liczba3)