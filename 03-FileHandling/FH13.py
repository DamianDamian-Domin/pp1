'''
program
'''

tablica = [32, 16, 5, 8, 24, 7]
index = -1
with open('liczby.txt', 'w') as file:
    for x in range(-1, 5):
        index = index + 1
        file.write(str(tablica[index]) + "\n")

