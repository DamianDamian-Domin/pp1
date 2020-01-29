import math
flag = True
while flag == True:
  try:  
    a = float(input("Wprowadź liczbę: "))
    assert a > 0
    print(f'Pierwiastek kwadratowy z liczby {a} wynosi {math.sqrt(a):.2f}')
    flag = False
  except:
    print("Podaj liczbę większą od 0")
 