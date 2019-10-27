'''
program
'''

a = int(input("Wprowadź długość boku a= "))
b = int(input("Wprowadź długość boku b= "))

for x in range(0, b):
    print("*", end="")
print()
for x in range(0, a-2):
    print("*",(b - 4) *" ","*")

for x in range(0, b):
    print("*", end="")

