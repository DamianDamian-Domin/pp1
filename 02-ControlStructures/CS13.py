'''
program
'''

x = int(input("Wprowadź współrzędną x: "))
y = int(input("Wprowadź współrzędną y: "))

if x > 0 and y > 0:
    print("Punkt znajduje się w ćwiartce pierwszej")
elif x < 0 and y > 0:
    print("Punkt znajduje się w ćwiartce drugiej")
elif x < 0 and y < 0:
    print("Punkt znajduje się w ćwiartce trzeciej")
else:
    print("Punkt znajduje się w ćwiartce czwartej")            
