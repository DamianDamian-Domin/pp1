class Pracownik:
    def __init__(self, osoba, staz_pracy, wynagrodzenie):
        assert type(staz_pracy) == int, 'Staż pracy nie jest liczbą'
        assert staz_pracy >= 0, 'Staż pracy nie może być mniejsze od 0'
        assert type(wynagrodzenie) == int, 'Wynagrodzenie nie jest liczbą'
        assert wynagrodzenie >= 0, 'Wynagrodzenie nie może być mniejsze od 0'
        self.osoba = osoba
        self.staz_pracy = staz_pracy
        self.wynagrodzenie = wynagrodzenie
    def __str__(self):
        return 'Imie i nazwisko: {}\nStaż pracy: {}\nWynagrodzenie: {}PLN\nDodatek: {}\nWynagrodzenie łączne: {}PLN'.format(
            self.osoba,
            self.staz_pracy,
            self.wynagrodzenie,
            self.dodatek(),
            self.wynagrodzenie + self.dodatek()
        )    
    def dodatek(self):
        if self.staz_pracy > 5:
            premia = (self.staz_pracy - 5) * 0.01
            if premia >= 0.2:
                premia = 0.2
        else:
            return 0        
        dopłata = premia * self.wynagrodzenie
        return dopłata

pracownik1 = Pracownik("Damian Domin", 20, 2800)
print(pracownik1)

