'''
program
'''

oceny = ["niedostateczny", "dopuszczający", "dostateczny", "dobry", "bardzo dobry", "celujący"]

ocena = int(input("Podaj ocenę: "))

if ocena == 1:
    print("Ocena słownie:",oceny[0])
elif ocena == 2:
    print("Ocena słownie:",oceny[1])
elif ocena == 3:
    print("Ocena słownie:",oceny[2])  
elif ocena == 4:
    print("Ocena słownie:",oceny[3])  
elif ocena == 5:
    print("Ocena słownie:",oceny[4])
elif ocena == 6:
    print("Ocena słownie:",oceny[5])
else:
    print("Nieprawidłowa ocena")            