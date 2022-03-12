class Person:
    counter = 0
    def __init__(self, name, surname, id, age ):
        self.name = name
        self.surname = surname
        self.id = id
        self.age = age
        Person.counter += 1
    
    def __str__(self):
        print(f'Namn: {self.name}\nEfternamn: {self.surname}\nID: {self.id}\nÅlder: {self.age}\n')

    def countPeople(self):
        print(f'Antal registrerade personer: {self.counter}')

p1 = Person('Martin', 'Liden', '9407', 27)
p2 = Person('Olivia', '??', '??', '??')
p2.countPeople()
p3 = Person('Slinky', '??', '??', '??')
p3.countPeople()
p2.countPeople()
p1.__str__()
p2.__str__()