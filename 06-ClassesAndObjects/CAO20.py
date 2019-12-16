'''
program
'''

from classes import lot

samolot1 = lot("LOT881")

samolot1.start()
samolot1.flight_status()
samolot1.height_up(8900)
samolot1.flight_status()
samolot1.height_down(200)
samolot1.flight_status()
samolot1.land()
samolot1.flight_status()
samolot1.height_down(8300)
samolot1.flight_status()
samolot1.land()
samolot1.flight_status()




