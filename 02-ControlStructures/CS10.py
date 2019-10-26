'''
program
'''

x = int(input("Wprowadź lcizbę całkowitą x="))

if x > 0:
    print("Liczba jest dodatnia")
else:
    print("Liczba jest ujemna lub równa 0")    
    if x % 2 != 0:
      print("Oraz jest nieparzysta") 
    else:
      print("Oraz jest parzysta")   
