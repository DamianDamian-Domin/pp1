'''
program
'''

tablica = ["zero", "jeden", "dwa", "trzy", "cztery", "pięc", "sześć", "siedem", "osiem", "dziewięc"]

liczba = input("Wprowadź liczbę: ")

print(f'{liczba} - ', end="")
for x in liczba:
    print(tablica[int(x)], end=" ")    

