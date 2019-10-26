'''
program
'''

login = "marek"
hasło = "m-123"

log = input("Wprowadź login: ")
pasw = input("Wprowadź hasło: ")

if log != login or hasło != pasw:
    print("Dane są nieprawidłowe")
else:
    print("Zalogowano")    
   