'''
program
'''

from classes import Telewizor

listaprogramow = ["TVP1", "TVP2", "Polsat", "TVN", "Polsat"]

p1 = Telewizor()
p1.show_status()
p1.On()
p1.set_channels(listaprogramow)
p1.show_channels
p1.set_channel(2)
p1.set_volume(5)
p1.show_status()
p1.set_channel(3)
p1.volume_up()
p1.show_status()
p1.volume_down()
p1.show_status()


