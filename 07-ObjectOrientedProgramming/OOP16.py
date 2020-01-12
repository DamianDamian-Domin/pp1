from classes import student

s1 = student("Anna", "Tomaszowska", 141820)
s2 = student("Wojciech", "Zbych", 201003)
s3 = student("Maja", "Kowalska", 153202)
s4 = student("Marek", "Migiel", 138600)

s1 == s2
s1 <= s2
print()
print(s1)
print()
print(s2)
print()
print(s3)
print()
print(s4)
print()
student.sort(s1,s2,s3,s4)

