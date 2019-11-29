'''
program
'''
tablica = []
with open("numbersinrows.txt") as file:
    for line in file:
        tablica += line.split(',')
tablica = [int(x) for x in tablica]

print("Ilość liczb: {} suma liczb {}".format(len(tablica), sum(tablica)))
