from message import Message
class mail(Message):
    def __init__(self, mail):
        self.mail = mail
        self.mail2 = ''
        self.topic = ''
        super().__init__()
    def send(self):
        self.mail2 = input("Podaj adres email do którego chcesz wysłać wiadmość: ")
        self.topic = input("Podaj temat adresu: ")
        print(f'Wysyłanie wiadomości..\nOd: {self.mail}\nDo: {self.mail2}\nTemat: {self.topic}\nTreść: {self.message}') 

