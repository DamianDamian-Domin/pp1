'''
program
'''
sp = 0
sn = 0

for x in range(1, 51):
    if x % 2 == 0:
        sp = sp + x
    else:
        sn = sn + x  

print(f"Suma liczb parzystych wynosi {sp} suma liczb nieparzystych wynosi {sn}")          
    