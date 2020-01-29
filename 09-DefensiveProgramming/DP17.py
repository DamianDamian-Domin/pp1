tab = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
flag = True
while flag == True:
   try:
       x = int(input("Wprowadź numer dnia tygodnia: "))
       if x not in range(1,8):
           raise ValueError
       print(f"Dzień tygodnia: {tab[x-1]}")
       flag = False 
   except:
       print("Nieprawidłowa wartość")
