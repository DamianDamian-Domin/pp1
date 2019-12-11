'''
program
'''

dochod1 = float(input("Wprowadź wartość dochodu: "))
if dochod1 < 0:
    raise Exception("Dochód nie może być mniejszy od 0!")  
def podatek(dochod):
    x = dochod
    if x <= 5000:
        y = 0.17 * x
        print(f'Podatek wynosi: {y}')
    else:
        n = x - 5000
        y = 0.32 * n + 0.17 * 5000
        print(f'Podatek wynosi: {y}')


podatek(dochod1)
