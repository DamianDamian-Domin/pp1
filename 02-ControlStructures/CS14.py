'''
program
'''

x = float(input("Podaj wiek psa w ludzkich latach"))

if x <= 2:
    print("Wiek psa w psich latach wynosi:{}".format(x * 10.5))
else:
    print("Wiek psa w psich latach wynosi: {}".format(4 * (x-2) + 21))    