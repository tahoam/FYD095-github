class Klass:
    def __init__(self, k, v):
        self.tab = dict()
        self.add(k,v)

    def add(self, k, v):
        self.tab[k] = v
    
    def edit(self, k, v):
        self.tab[k] = v
    
    def remove(self, k):
        del self.tab[k]
    
    def printDict(self):
        print(self.tab)

d1 = Klass('1', 1)
d1.add('hej', 'san')
d1.printDict()
d1.add('hejsan', 17)
d1.printDict()
d1.edit('hej', 'då')
d1.printDict()
d1.remove('hej')
d1.printDict()