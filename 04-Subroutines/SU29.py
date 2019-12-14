'''
program
'''

tablica = [2, 3, 5, 2, 9, 8 ,1 ,3, 9, 1, 1, 4, 7, 7, 1, 4, 4, 4,]
def mediana():
    if len(tablica)%2 == 0:
        tablica.sort()
        x = int(len(tablica)/2)
        y = x - 1
        m = (tablica[x] + tablica[y]) / 2
        return m
    else:
        tablica.sort()
        print(tablica)    
        x = int(len(tablica)/2)
        print(x)
        m = tablica[x]
        return m
def dominata():
    tablica.sort()
    var = 0
    liczba = 0   
    for x in range (0, 10):
        y = tablica.count(x) 
        if y > var:
            var = y
            liczba = x               
    return liczba
p = input("Wybierz funkcje: mediana/dominata: ") 
if p == "mediana":
    print(f'Mediana wynosi: {mediana()}')
elif p == "dominata":
    print(f'Dominata wynosi: {dominata()}')
else:
    raise Exception("Brak takiej funkcji")


            
        


