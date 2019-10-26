'''
program
'''

imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]

temp = 0
imie_index = None
for i in imiona:
    if len(i) > temp:
        temp = len(i)
        imie_index = imiona.index(i)
print(f'Najdłuższe imię w tablicy to {imiona[imie_index]}')    

