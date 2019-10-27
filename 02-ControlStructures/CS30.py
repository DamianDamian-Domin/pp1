'''
program
'''

pin = "0805"
blokada = 0

for x in range(3):
    pinenter = input("Wprowadź pin") 
    if pin == pinenter:
        print("Pin prawidłowy")
        print("Zalogowano")
        break
    else:
        blokada += 1
        print("Pin niepoprawny")
if blokada == 3:
    print("Karta zablokowana")        
        

    

   
    
     
