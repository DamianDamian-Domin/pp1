'''
program
'''

tablica = []
with open('universities.txt') as file:
    for line in file:
        tablica.append(line.strip('"\n'))
tablica.sort()
print(tablica)
with open('universities.txt', "w") as file:
    for x in tablica:
       file.write(x + "\n")
       
