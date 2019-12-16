class University():
    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'

    def print_name(self):
        print(self.name)

    def set_name(self, new_name):
        self.name = new_name 

    def print_fullname(self):
        print(self.fullname)

    def set_fullname(self, new_name):
        self.fullname = new_name

class Telewizor():
    def __init__(self):
        self.is_on = 0
        self.channel = 1
        self.channels = []
        self.volume = 0

    def On(self):
        self.is_on = 1

    def Off(self):
        self.is_on = 0

    def set_channel(self, channel):
        self.channel = channel

    def set_channels(self, channels_list):
        self.channels = channels_list

    def set_volume(self, volume):
        self.volume = volume 

    def volume_up(self):
        self.volume +=1

    def volume_down(self):
        self.volume -=1           

    def show_channels(self):
        print(self.channels)

    def show_status(self):
        if self.is_on == 1:
            print(f"Telewizor jest włączony\nUstawiony kanał: {self.channel} ({self.channels[self.channel - 1]})\nGłośność = {self.volume}/10")
        else:
            print("Telewizor jest wyłączony")

class book():
    def __init__(self, title, autor, page_numbers):
        self.title = title
        self.autor = autor
        self.page_numbers = page_numbers
        self.page_number = 0
        self.is_open = 0
    def book_open(self):
        self.isopen = 1
    def book_close(self):
        self.isopen = 0
    def book_info(self):
         if self.isopen == 1:
             print(f'Autor książki: {self.autor}\nTytuł książki: {self.title}\nIlość stron: {self.page_numbers}\nAktualna strona: {self.page_number}')
         else:
             print(f'Autor książki: {self.autor}\nTytuł książki: {self.title}\nIlość stron: {self.page_numbers}\nAktualna strona: Książka jest zamknięta')  
    def read_page(self):
        if self.isopen == 1:
              self.page_number += 1
        else:
            print("Książka jest zamknięta")
    def back_page(self):
        if self.isopen == 1:
              self.page_number -= 1
        else:
            print("Książka jest zamknięta")                  
    def skip_to_page(self, x):
        if self.isopen == 1:
            self.page_number = x
        else:
            print("Książka jest zamknięta")

class ułamki():
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def number_show(self):
        print(f"Ułamek wynosi: {self.licznik}/{self.mianownik}")
    def uprość_ułamek(self):
        x = NWD(self.licznik, self.mianownik)
        self.licznik = int(self.licznik/x)
        self.mianownik = int(self.mianownik/x)

def NWD(a, b):
    c = 0
    while b != 0:
        c = a % b
        a, b = b, c
    return a 

class kostka():
    def __init__(self, numer):
        self.oczka = 1
        self.numer = numer
    def rzuć_kostką(self):
        from random import randint
        self.oczka = randint(1, 6)
        return self.oczka 

class konto():
    def __init__(self, nr_rachunku):
        self.nr_rachunku = nr_rachunku
        self.saldo = 0
    def stan(self):
        print(f'Twój numer rachunku: {self.nr_rachunku}\nStan konta: {self.saldo}zł')
    def wpłata(self, x):
        self.saldo += x
    def wypłata(self, x):
        if x > self.saldo:
            print("Nie wystarczająca ilość środków na koncie")
        else:
            self.saldo -= x

class lot():
    def __init__(self, flight_number):
        self.flight_number = flight_number
        self.is_in_air = 0
        self.height = 0
    def land(self):
        if self.height < 500:
            self.is_in_air = 0
            print("Wylądowano pomyślnie")
        else:
            print("Za duża wysokość, zmniejsz pułap")
    def start(self):
            self.is_in_air = 1
            print("Wylądowano pomyślnie")    
    def height_up(self, x):
        if self.is_in_air == 1:
             self.height += x
        else:
            print("Samolot nie jest w powietrzu")     
    def height_down(self, x):
        if self.is_in_air == 1:
             self.height -= x
        else:
            print("Samolot nie jest w powietrzu")
    def flight_status(self):
        if self.is_in_air == 1:
            print(f"Tu {self.flight_number}, moja wyskość lotu to: {self.height}")
        else:
            print("Samolot na pasie startowym") 








         
