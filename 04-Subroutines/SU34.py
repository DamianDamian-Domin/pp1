'''
program
'''


def fib(n):     
    a,b = 0,1     
    for i in range(n-1):         
        a,b = b,a+b     
    return a

tablica = [fib(x) for x in range(0, 20)]
print(tablica)  