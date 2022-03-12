class Vektor:
    def __init__(self, x, y, z):
        self.coord = (x, y, z) 
    
    def add(self, v2):
        self.coord = (self.coord[0] + v2[0], self.coord[1] + v2[1], self.coord[2] + v2[2])


    def subtract(self, v2):
        self.coord = (self.coord[0] - v2[0], self.coord[1] - v2[1], self.coord[2] - v2[2])
    
    def dotProduct(self, v2):
        self.coord = (self.coord[0] * v2[0], self.coord[1] * v2[1], self.coord[2] * v2[2])

    def crossProduct(self, v2):
        x = self.coord[1]*v2[2]-self.coord[2]*v2[1]
        y = self.coord[2]*v2[0]-self.coord[0]*v2[2]
        z = self.coord[0]*v2[1]-self.coord[1]*v2[0]
        self.coord = (x,y,z)

    def printVector(self):
        print(f'x: {self.coord[0]}\ny: {self.coord[1]}\nz: {self.coord[2]}\n')
        
    def getVector(self):
        return self.coord

v1 = Vektor(1,1,1)
v2 = Vektor(1,2,3)
v3 = Vektor(1,1,1)

v1.printVector()

v1.add(v2.getVector())
v1.printVector()

v1.subtract(v2.getVector())
v1.printVector()

v1.dotProduct(v2.getVector())
v1.printVector()

v1.crossProduct(v2.getVector())
v1.printVector()

v1.add(v2.getVector())
v1.printVector()

v1.crossProduct(v3.getVector())
v1.printVector()