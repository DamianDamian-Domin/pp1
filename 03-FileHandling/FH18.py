'''
program
'''
tablica = []
with open('numbers.txt') as file:
    for line in file:
        tablica.append(int(line))
tablica.sort()        
print(tablica)        
