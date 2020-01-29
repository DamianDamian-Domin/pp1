try:
    with open("NoEducation.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("Plik nie został odnaleziony")  
except OSError:
    print("Błąd przy otwieraniu pliku")

