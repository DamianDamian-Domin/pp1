flag = True
while flag == True:
    try:
        imie = str(input("Wprowadź imie: "))
        nazwisko = str(input("Wprowadź nazwisko: "))
        if len(imie) < 3 or len(nazwisko) < 3:
            raise ValueError
        print(f"{imie} {nazwisko.upper()}")
        flag = False
    except:
        print("Wprowadzone dane są nieprawidłowe")    