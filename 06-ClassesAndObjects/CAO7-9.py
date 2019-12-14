'''
program
'''

class University():
    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'


    def print_name(self):
        print(self.name)

    def set_name(self, new_name):
        self.name = new_name 

    def print_fullname(self):
        print(self.fullname)

    def set_fullname(self, new_name):
        self.fullname = new_name    
               
p1 = University()
p2 = University()


p1.print_name()
p1.set_name("AGH")
p1.print_name()   

p2.print_fullname()
p2.set_fullname("Akademia Górniczo Hutnicza w Krakowie")
p2.print_fullname()                