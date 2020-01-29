student = 'Mateusz'
assert type(student) == str, "Nieprawidłwoe imie"
stypendium = 900
assert type(stypendium) == int or type(stypendium) == float, "Stypendium musi byc liczbą"
wydatki = 850
assert type(stypendium) == int or type(stypendium) == float, "Wydatki muszą byc liczbą"

print('Student: {}'.format(student.upper()))
print('stypendium: {} zł'.format(stypendium))
print('Wydatki: {} zł'.format(wydatki))
print('Oszczędności: {} zł'.format(stypendium-wydatki))