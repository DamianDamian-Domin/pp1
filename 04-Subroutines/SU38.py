'''
program
'''

def wl(zdanie):
    upper = []
    for x in zdanie:
        if x.isupper():
            upper.append(x)
    return ''.join(upper)

zdanie1 = str(input("Wprowadź zdanie: "))
print(wl(zdanie1))
