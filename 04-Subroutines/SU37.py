'''
program
'''

def rec(tab):
    t1 = []
    t2 = []
    for x in tab:
        if x not in t1:
            t1.append(x)
            t2.append(x)
        else:
            t2.remove(x)
    return t2

lista = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8]
print(rec(lista))

