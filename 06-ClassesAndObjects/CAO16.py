'''
program
'''

#Aby utworzyć książke nadaj jej:
    #Tytuł, autora oraz ilość stron
#Dostępne funkcje:
#book_open()
#book_close()
#book_info()
#read_page()
#back_page()
#skip_to_page()

from classes import book

książka = book("Malowany człowiek", "Adam Wabger", 675)

książka.book_open()
książka.book_info()
książka.read_page()
książka.read_page()
książka.read_page()
książka.read_page()
książka.book_info()
książka.book_close()
książka.read_page()
książka.book_info()
