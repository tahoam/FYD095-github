from cmath import inf
import math

class Point:
    def __init__(self,x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        print(f'Punkten har koordinterna:\nx: {self.x}\ny: {self.y}\nz: {self.z}')
    
    def Avstand(self):
        return((self.x**2 + self.y**2 + self.z**2)**(0.5))

    def Sfariska(self):
        r = self.Avstand()
        if r != 0:
            phi = math.acos(self.z/r)
        else:
            print('Point in origin..')
            phi = 0.0
        theta = math.atan2(self.y, self.x)
        return (r, phi, theta)
    

p1 = Point(1, 0, 0)
p2 = Point(2, 2, 2)
p3 = Point()
p1.__str__()
print(p1.Sfariska())
print(p1.Avstand())
p2.__str__()
print(p2.Sfariska())
print(p2.Avstand())
p3.__str__()
print(p3.Sfariska())
print(p3.Avstand())