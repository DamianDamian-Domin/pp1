from message import Message
class SMS(Message):
    def __init__(self, number):
        self.number = number
        self.number2 = ""
        super().__init__()
    def send(self):
        self.number2 = input("Podaj numer odbiorcy: ")

        print(f"Wysyłanie wiadomości z numeru: {self.number}\nNa numer: {self.number2}\nWiadomość: {self.message}")
       

        

