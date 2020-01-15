from classes import pojazd, samochod_osobowy, samochod_dostawczy, rental

pojazd1 = samochod_osobowy("Seat Leon", "KRN100500", "5")
pojazd2 = samochod_dostawczy("Dacia Duster", "KRP250300", "10" )
pojazd3 = samochod_osobowy("Citroen Xsara", "KR200100", "5" )
wypożyczalnia1 = rental("Car Boss", pojazd1, pojazd2)

print(wypożyczalnia1)
wypożyczalnia1.rent("KRP250300")
wypożyczalnia1.show_free()
wypożyczalnia1.show_rented()




