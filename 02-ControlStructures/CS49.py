'''
program
'''

nrDniaTygodnia = 0
dni = ['PN','WT','SR','CZ','PT','SB','ND']

print('|', end=' ')

for x in range(0,7):
    print(dni[x], end=' | ')
week = 1
print()
for x in range(0,42):
    if nrDniaTygodnia != 6 and x > 34:
        break
    print('|', end='')
    if x < nrDniaTygodnia or x-nrDniaTygodnia+1 > 30:
        print('    ', end='')
    else:
        print((' {:2d} ').format(x-nrDniaTygodnia+1), end='')
    
    if week % 7 == 0:
        print('|')
    week += 1