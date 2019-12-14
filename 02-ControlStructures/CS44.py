''''
program
'''

V1 = int(input("Podaj limit prędkości: "))
V2 = int(input("Podaj prędkość pojazdu: "))
V3 = V2 - V1

if V3 <= 0:
    print("Brak mandatu")
elif V3 <= 10:
    for x in range(V3 + 1):
        x = x * 5
    print(f'Mandat wynosi {x} zł') 
else:
    for x in range(V3 + 1):
        x = x * 15
    print(f'Mandat wynosi {x} zł')         