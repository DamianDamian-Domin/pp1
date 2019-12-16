def NWD(a, b):
    c = 0
    while b != 0:
        c = a % b
        a, b = b, c
    return a

print(NWD(12, 21))  

