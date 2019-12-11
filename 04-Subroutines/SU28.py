'''
program
'''

języki = ["      Java:", "    Python:", "JavaScript:", "       C++:", "        C#:", "      Ruby:", "      Perl:", "       PHP:", "         C:", "   Android:"]
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
y = -1
for x in języki:
    y += 1
    print(x + " " + (wartosci[y] * "#"))