'''
program
'''
tablica = []
with open('numbers.txt') as file:
    for line in file:
        if int(line) % 2 == 0:
            tablica.append(int(line))
with open('evennumbers.txt', 'w') as file:
    for x in tablica:
        file.write(str(x) + "\n")     


