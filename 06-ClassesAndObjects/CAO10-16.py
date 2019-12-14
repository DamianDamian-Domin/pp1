'''
program
'''

class Telewizor():
    def __init__(self):
        self.is_on = 0
        self.channel = 1
        self.channels = []
        self.volume = 0

    def On(self):
        self.is_on = 1

    def Off(self):
        self.is_on = 0

    def set_channel(self, channel):
        self.channel = channel

    def set_channels(self, channels_list):
        self.channels = channels_list

    def set_volume(self, volume):
        self.volume = volume 

    def volume_up(self):
        self.volume +=1

    def volume_down(self):
        self.volume -=1           

    def show_channels(self):
        print(self.channels)

    def show_status(self):
        if self.is_on == 1:
            print(f"Telewizor jest włączony\nUstawiony kanał: {self.channel} ({self.channels[self.channel - 1]})\nGłośność = {self.volume}/10")

        else:
            print("Telewizor jest wyłączony")

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


