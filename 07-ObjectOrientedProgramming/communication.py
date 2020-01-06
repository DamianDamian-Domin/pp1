from mail import mail
from SMS import SMS


w1 = SMS("518715394")
e1 = mail("dymek662@tlen.pl")

w1.set_message("Wiadomość testowa")
e1.set_message("Wiadomość testowa")
w1.send()
e1.send()


