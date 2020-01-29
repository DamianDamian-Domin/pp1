cyfry = ["0","1","2","3","4","5","6","7","8","9",]
flag = True
while flag == True:
    try:
        pesel = input("Wprowadź pesel: ")
        if len(pesel) != 11:
            raise ValueError
        for x in pesel:
            if x not in cyfry:
                raise ValueError
        print(pesel)    
        flag = False    
    except ValueError:
        print("Podany pesel jest nieprawidłowy")        
