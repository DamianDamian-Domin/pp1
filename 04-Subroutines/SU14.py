'''
program
'''

def wystepuje(liczba, tablica):
    print(f'Liczba: {liczba}')
    print(f'Tablica: {tablica}')
    if liczba in tablica:
        print("Podana liczba występuje w tablicy")
    else:
        print("Podana liczba nie występuje w tablicy")
liczba = 23
tablica = [15, 38, 7, 23, 14] 
wystepuje(liczba, tablica)           