try:
    h = int(input('Wzrost w cm: '))
except (ValueError):
    print('Wzrost nie jest liczbą całkowitą')
    exit()

assert int(h) in range(150, 221), 'Wzrost poza skalą 150-220'

try:
    w = float(input('Waga w kg: '))
except ValueError:
    print('Waga nie jest liczbą rzeczywistą')
    exit()

assert 40.0 <= w <= 150.1, 'Waga poza skalą 40.0-150.0'
bmi = w/(h/100)**2
print('Wzrost: {}cm\nWaga: {}kg\nBMI: {:.2f}'.format(h, w, bmi))