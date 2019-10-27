class LessThanOneError(Exception):
    """ Błąd gdy N < 1 """
    pass

try:
    n = int(input('Podaj N: '))
    if n < 1:
        raise LessThanOneError
    x = 0
    liczba = 1
    
    print('Liczby pierwsze: ', end='')
    while x < n:
        flag = True
        if liczba == 2:
            print(liczba, end=' ')
            x += 1
        elif liczba > 2:
            for d in range(2,liczba):
                if liczba % d == 0:
                    flag = False
                    break
            if flag == True:
                print(liczba, end=' ')
                x += 1
        liczba += 1



except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except LessThanOneError:
    print('N nie może być mniejsze do 1!')