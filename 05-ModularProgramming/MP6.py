'''
program
'''

import csv 
with open('employees.csv', newline='') as f:     
    reader = csv.reader(f)
    x = 0 
    flag = 0    
    for row in reader:
        if flag == 0:
            print(f'# {row[1].upper()}           {row[0].upper()}            {row[2].upper()}          {row[3].upper()}\n{"=" * 75}')
            flag += 1
        else:
            x+=1
            print(f"{x} {'          '.join(row)}")    