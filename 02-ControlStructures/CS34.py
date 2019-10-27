'''
program
'''

pesel = input("Wprowadź numer pesel")

płeć = int(pesel[9])
rok = pesel[0] + pesel[1]

if płeć in [1, 3, 5, 7, 9]:
    płeć = "mężczyzna"
else:
    płeć = "kobieta" 

if int(rok) <= 99 and int(rok) >= 18: 
    rok = "19" + str(rok) 
else:
    rok = "20" + str(rok)   

wiek = 2018 - int(rok)

print(f'Osoba o numerze {pesel}\n Płeć = {płeć}\n Wiek = {wiek}')

      