'''
program
'''

from classes import University            
               
p1 = University()
p2 = University()


p1.print_name()
p1.set_name("AGH")
p1.print_name()   

p2.print_fullname()
p2.set_fullname("Akademia Górniczo Hutnicza w Krakowie")
p2.print_fullname()                