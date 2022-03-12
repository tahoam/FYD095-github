class Person:
    def __init__(self, name, id ):
        self.name = name
        self.id = id
    
    def __str__(self):
        print(f'En person!\nNamn: {self.name}\nID: {self.id}\n')

class Bilist(Person):
    def __init__(self, name, id, cert = 'B'):
        super().__init__(name, id)
        self.cert = cert
    def __str__(self):
        print(f'En bilist!\nNamn: {self.name}\nID: {self.id}\nKörkort: {self.cert}\n')


p1 = Bilist('Martin', '9407')
p2 = Person('Olivia', '??')
p3 = Bilist('Slinky', '??', 'C')
p1.__str__()
p2.__str__()
p3.__str__()

