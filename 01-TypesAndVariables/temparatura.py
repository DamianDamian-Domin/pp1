'''
Zamiana temperatury na Fahrenheity oraz Kelviny
'''

C = float(input('podaj temperature w celcjuszach')) #temperatura w Celcjuszach
F = C * 1.8 + 32 #temperatura w Fahrenheitach
K = C + 273.15 #temperatura w Kelvinach

tempF = ("Temperatura w Fahrenheitach dla {} stopni celcjusza wynosi {}")
tempK = ("Temperatura w Kelvinach dla {} stopni celcjusza wynosi {}")

#rezultaty

print(tempF.format(C, F))
print(tempK.format(C, K))