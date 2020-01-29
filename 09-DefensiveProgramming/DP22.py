import csv

students = []
with open('students.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
     assert len(row) == 4, 'Plik nie jest pełny'
    for val in row:
         assert val != '', 'Pusta wartość'
         students.append(row)

for elem in students:
    print(', '.join(elem))
