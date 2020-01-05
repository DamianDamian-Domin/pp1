class muzyka():
    def __init__(self, wykonawca, utwór, album, rok):
        self.wykonawca = wykonawca
        self.utwór = utwór
        self.album = album
        self.rok = rok
    def __str__(self):
        return "Wykonawca: " + self.wykonawca + "\n" + "Utwór: " + self.utwór + "\n" + "Album: " + self.album + "\n" + "Rok: " + self.rok
class Studenci():
    uczelnia = "UEK Kraków"
    uid = 100000
    def __init__(self, name, kierunek):
        self.suid = Studenci.uid
        self.name = name
        self.kierunek = kierunek
        Studenci.uid += 1
    def __str__(self):
        return self.name + " (" + str(self.suid) + ") " + self.kierunek + " "+ Studenci.uczelnia             


