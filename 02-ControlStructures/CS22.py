'''
program
'''
s = 0
i = 0

tablica = [15, 8, 31, 47, 2, 19]

for x in tablica:
    if x % 2 != 0:
        s = s + x
        i = i + 1 

sr = s/i

print(f'Średnia atytmetyczna liczb nieparzystych wynosi {sr}')


