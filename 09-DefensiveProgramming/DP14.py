def pole_prostokata(a,b):
    try:
        if a<=0 or b <=0:
            raise ValueError
        else:
            return a*b
    except:
        return "Podane wartości są nieprawidłowe"

try:
    a = float(input("Podaj wartość a: "))
    b = float(input("Podaj wartość b: "))
    print(pole_prostokata(a, b))
except ValueError:
    print("Podane wartości nie są liczbami")
    exit()            

