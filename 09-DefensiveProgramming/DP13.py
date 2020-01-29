netto = 150

if (type(netto)!=int and type(netto)!=float) or netto < 0:
    raise TypeError("Niepoprawna cena")

brutto = 0.23 * netto + netto
print(f'Cena netto: {netto}\nCena brutto: {brutto}')


