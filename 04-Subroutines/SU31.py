'''
program
'''

def odwr(tab):
    newtab = [x for x in tab[::-1]]
    return newtab

tablica = [2, 5, 4, 1, 8, 7, 4, 0, 9]

print(tablica,odwr(tablica))

