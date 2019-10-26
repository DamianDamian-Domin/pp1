'''
program
'''
n = int(input("Wprowadź liczbę n początkowych wyrazów: "))

a = 1
for x in range(1, n+1):
    print(a, end=', ')
    a = a + 3
