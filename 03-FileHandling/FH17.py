'''
program
'''

import re

komunikat = "To be, or not to be, that is the question"
spł = re.findall('[aeyuioóąę]', komunikat)

print(len(spł))