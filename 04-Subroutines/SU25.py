'''
program
'''

tablica1 = ["Janek", "Ania", "Wojtek", "Zosia"]
imie1 = "Wojtek"
def jestImie(imie, imiona):
    x = imiona
    y = imie
    if y in x:
        print("Imie zawarte w spisie imion")
    else:
        print("Imie nie zawarte w spisie imion")  
jestImie(imie1, tablica1)          

