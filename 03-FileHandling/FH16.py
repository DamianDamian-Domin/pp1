'''
program
'''

import re 
komunikat = 'wtorek -23C, środa -17C, czwartek 25C' 
cyfry = re.findall('[-]*\d{2}',komunikat)
cyfry = [int(x) for x in cyfry]
suma = sum(cyfry)/3
print(suma)


