'''
program
'''
limit = int(input('Podaj limit prędkości (km/h): '))
predkosc = float(input('Podaj prędkość pojazdu (km/h): '))
przekroczenie = predkosc - limit
if przekroczenie <= 0:
        mandat = 0
    elif przekroczenie <= 10:
        mandat = przekroczenie*5
    else:
        mandat = 10*5 + (przekroczenie-10)*15
        
    print('Mandat (zł): {:.2f}'.format(mandat))    