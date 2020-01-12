'''
program
'''
from random import randint

nikolka = [
    "Jessie", "Rosa", "Tara", "Shelly", "El Primo", "Darryl", "Poko", "Penny", "Nita", "Bull", "Carl", "Piper",
     "Jhin", "Colt", "Boo", "Brock", "Barley", "Dynamike", "Tick", "Rico"]

damianek = ["Jessie", "Rosa", "Shelly", "El Primo", "Darryl", "Poko", "Penny", "Nita", "Bull", "Carl", "Colt", "Brock", "Barley", "Dynamike", "Rico", "Bibi"]

f1 = randint(0, len(nikolka)-1)
f2 = randint(0, len(damianek)-1)

print(f'Postać Nikoli: {nikolka[f1]}\nPostać Damiana: {damianek[f2]}')


   