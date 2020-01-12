from random import randint
from math import sqrt, pi
class muzyka():
    def __init__(self, wykonawca, utwór, album, rok):
        self.wykonawca = wykonawca
        self.utwór = utwór
        self.album = album
        self.rok = rok
    def __str__(self):
        return "Wykonawca: " + self.wykonawca + "\n" + "Utwór: " + self.utwór + "\n" + "Album: " + self.album + "\n" + "Rok: " + self.rok
class Studenci():
    uczelnia = "UEK Kraków"
    uid = 100000
    def __init__(self, name, kierunek):
        self.suid = Studenci.uid
        self.name = name
        self.kierunek = kierunek
        Studenci.uid += 1
    def __str__(self):
        return self.name + " (" + str(self.suid) + ") " + self.kierunek + " "+ Studenci.uczelnia
class Phone():
    def __init__(self, model, numer):
        self.model = model
        self.numer = numer
        self.serial_number = []
        self.ison = 0
        for x in range(10):
            self.serial_number.append(randint(0, 9))
        self.serial_number = "".join(str(cyfra) for cyfra in self.serial_number)    
    def __str__(self):
        return f'Model telefonu = {self.model}\nNumer telefonu = {self.numer}\nNumer seryjny: {self.serial_number}'
    def phone_on(self):
        self.ison = 1
    def phone_off(self):
        self.ison = 0
    def call_to(self, numer):
        if self.ison == 1:
            print(f"Wybieraniu numeru: {numer}...")
        else:
            print("Telefon wyłączony")
class Book():
    def __init__(self, tytuł, autor, rok):
        self.tytuł = tytuł
        self.autor = autor
        self.rok = rok
class OldBook(Book):
    def __init__(self, tytuł, autor, rok, pages):
        self.pages = pages
        super().__init__(tytuł, autor, rok) 
    def __str__(self):
        return 'Książka klasyczna - Tytuł: {}\nAutor: {}\nRok: {}\nIlość stron: {}'.format(
            self.tytuł,
            self.autor,
            self.rok,
            self.pages
        )
class E_book(Book):
    def __init__(self, tytuł, autor, rok, plik):
        self.plik = plik
        super().__init__(tytuł, autor, rok)
    def __str__(self):
        return 'Książka elektroniczna - Tytuł: {}\nAutor: {}\nRok: {}\nNazwa pliku: {}'.format(
            self.tytuł,
            self.autor,
            self.rok,
            self.plik
        )
class student():
    @staticmethod
    def sort(*args):
        for e in sorted(list(args), key=lambda student: student.numer_albumu):
            print(e)
            print()
    def __init__(self, imie, nazwisko, numer_albumu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_albumu = numer_albumu        
    def __str__(self):
        return  "{}\n{}\n{}".format(self.imie, self.nazwisko, self.numer_albumu) 
    def __eq__(self, other):
        if self.numer_albumu == other.numer_albumu:
            print("Studenci mają ten sam numer albumu")
        else:
            print("Studenci mają różne numery albumów")  
    def __le__(self, other):
        if self.numer_albumu <= other.numer_albumu:
            print("Student {} {} ma mniejszy numer albumu od studenta {} {}".format(
                self.imie,
                self.nazwisko,
                other.imie,
                other.nazwisko
            ))
class maths():
    @staticmethod
    def circle(r):
        p = pi * r**2
        return f'Pole wynosi: {p:.2f}'
    def rectangle(a, b):
        p = a * b
        return f'Pole wynosi: {p:.2f}'
    def triangle(a, h):
        p = (a * h)/2
        return f'Pole wynosi: {p:.2f}'        





            


   



