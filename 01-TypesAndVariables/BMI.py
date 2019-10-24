'''
Program do liczenia BMI
'''

wzrost = float(input("Wprowadź wzrost w metrach"))  #wzrost
waga = float(input("Wprowadź wagę w kilogramach"))  #waga
BMI = waga/wzrost**2                                #BMI

#rezultat

if BMI >=18 and BMI <=25:
    print("BMI wynosi {:.2f} Waga prawidłowa".format(BMI))
else:
    print("BMI wynosi {:.2f} Waga nieprawidłowa".format(BMI))  