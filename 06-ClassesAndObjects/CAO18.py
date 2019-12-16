'''
program
'''
from classes import kostka

k1 = kostka(1)
k2 = kostka(2)
k3 = kostka(3) 

a = k1.rzuć_kostką()
b = k2.rzuć_kostką()
c = k3.rzuć_kostką()

print(f'Ilość oczek na pierwszej kostce: {a}\nIlość oczek na drugiej kostce: {b}\nIlość oczek na trzeciej kostce: {c}\nSuma oczek: {a + b + c}')