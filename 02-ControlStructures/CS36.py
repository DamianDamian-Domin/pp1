'''
program
'''

liczba = 0

for x in range(0, 100000):
    if ( 
        liczba % 7 == 0
        and liczba % 6 == 1
        and liczba % 5 == 1
        and liczba % 4 == 1
        and liczba % 3 == 1
        and liczba % 2 == 1
    ):
        print(liczba)
        break 
    else:
        liczba = liczba + 1        


