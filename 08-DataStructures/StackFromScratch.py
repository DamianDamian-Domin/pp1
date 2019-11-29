class Element:
    
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}'
    
    
class Stack:
    
    def __init__(self):
        self.top = None
        
    def pop(self):
        if not self.is_empty():
            element = self.top
            self.top = element.next
            return element
        return None
        
    def push(self,element):
        element.next = self.top
        self.top = element
        
    def is_empty(self):
        return self.top == None
    
    def __str__(self):
        stack = ''
        element = self.top
        while element != None:
            stack += str(element)+'\n'
            element = element.next
        return stack    


# utwórz stos
stack = Stack()

# dodaj elementy na stos
print('Dodaję na stos')
element = Element(5)
print(element)
stack.push(element)

element = Element("abc")
print(element)
stack.push(element)

element = Element(True)
print(element)
stack.push(element)

# pokaż stos
print(f'\nZawartość stosu\n{stack}')

# zdejmij ze stosu
print('Zdejmuję ze stosu')
print(stack.pop())

# pokaż stos
print(f'\nZawartość stosu\n{stack}')
