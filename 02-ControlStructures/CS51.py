'''
kalkulator
'''

while True:
    option = input("Wybierz funkcje:\nDodawanie: +\nOdejmowanie: -\nMnożenie: *\nDzielnie: /\nWyjście: quit\nFunkcja:  ")
    if option == "quit":
        break
    elif option == "+":
        x = int(input("Wprowadź wartość x: "))
        y = int(input("Wprowadź wartość y: "))
        print(x + y)
    elif option == "-":
        x = int(input("Wprowadź wartość x: "))
        y = int(input("Wprowadź wartość y: "))
        print(x - y)
    elif option == "*":
        x = int(input("Wprowadź wartość x: "))
        y = int(input("Wprowadź wartość y: "))
        print(x * y)
    elif option == "/":
        x = int(input("Wprowadź wartość x: "))
        y = int(input("Wprowadź wartość y: "))
        print(x / y)    

