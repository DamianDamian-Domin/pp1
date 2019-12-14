'''
program
'''

try:
    d = int(input("Podaj liczbę: "))
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą")
else:
    digits = []
    r = None
    i = d
    while i > 0:
        r = i%2
        digits.append(r)
        i = i//2
    digits.reverse()
    digits = (str(digit) for digit in digits)
    binary = ''.join(digits)
    print("{0}(10) = {1}(2)".format(d,binary))