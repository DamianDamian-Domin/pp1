from classes import pojazd, samochod_osobowy, samochod_dostawczy, rental

pojazd1 = samochod_osobowy("Seat Leon", "KRN100500", "5")
pojazd2 = samochod_dostawczy("Dacia Duster", "KRP250300", "10" )
pojazd3 = samochod_osobowy("Citroen Xsara", "KR200100", "5" )
pojazd4 = samochod_osobowy("Ford Fiesta", "KR216543", "4")
pojazd5 = samochod_dostawczy("Fiat Boxer", "KRY321232", "20")
wypożyczalnia1 = rental("Car Boss", pojazd1, pojazd2)

wypożyczalnia1.add_carrs(pojazd3, pojazd4, pojazd5)
print(wypożyczalnia1)
wypożyczalnia1.rent("KRN100500")
wypożyczalnia1.rent("KRY321232")
wypożyczalnia1.show_rented()
wypożyczalnia1.show_free()
wypożyczalnia1.derent("KRN100500")
wypożyczalnia1.show_rented()
wypożyczalnia1.show_free()






