import math as m


class Spherical:

    def __init__(self, r):
        self.radius = r

    def changeR(self, Radius):
        self.radius = Radius

    def findVolume(self):
        r = self.radius
        return (4 / 3) * 3.14 * (r * r * r)

    def findArea(self):
        r = self.radius
        return 4 * (3.14) * (r * r)

    def __str__(self):
        return 'Radius ={self.radius} Volume = '.format(self=self) + str(self.findVolume()) + ' Area = '+ str(self.findArea())

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)