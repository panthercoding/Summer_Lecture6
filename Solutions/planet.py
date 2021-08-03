import numpy as np 

""" helper function to calculate arc cosine given radians """
def arccosine(theta):
  return np.arccos(theta)

"""
the 3D point class as implemented in the handout, including
methods to calculate the traditional Euclidean distance
between two points as well as the more geographically
relevant great circle distance 
(distance along the surface of the Earth) 
"""
class Point3D():

  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def EuclideanDistance(self,other):
    """ calculate the Euclidean distance between two points
    and returns it (delete the below) """
    diff_x = self.x - other.x 
    diff_y = self.y - other.y 
    diff_z = self.z - other.z 

    return (diff_x**2 + diff_y**2 + diff_z**2)**0.5

  def greatCircleDistance(self,other):
    dist_point1_origin = self.EuclideanDistance(Point3D(0,0,0))
    dist_point2_origin = other.EuclideanDistance(Point3D(0,0,0))

    r = max(dist_point1_origin,dist_point2_origin)

    d_greatCircle = r * arccosine((self.x * other.x + self.y * other.y + self.z * other.z)/r**2)

    return d_greatCircle
  
  """ prewritten method to print out a 3D coordinate """
  def __str__(self):
    return "<{},{},{}>".format(self.x,self.y,self.z)
  
"""
the Planet class includes the center of the Planet as a 3D point,
the radius of the planet, and the number of inhabitants,
as well as a few methods inspired by ecology and cinema. 
"""
class Planet():

  def __init__(self,centerPoint,radius,inhabitants):

    self.centerPoint = centerPoint
    self.radius = radius 
    self.inhabitants = inhabitants
  
  def extinction(self):
    self.inhabitants = 0

  def ThanosWasHere(self):
    self.inhabitants = self.inhabitants // 2

  def growPopulation(self):
    self.inhabitants = self.inhabitants * 2

"""
the Moon class is a child class of Planet and 
hence borrows its methods. It is essentially
a Planet with 0 inhabitants and an extra
parameter called name. 
"""
class Moon(Planet):

  def __init__(self,centerPoint,radius,name):
    super().__init__(centerPoint,radius,0)
    self.name = name 
  
  def crashIntoPlanet(self,thePlanet):
    self.centerPoint = thePlanet.centerPoint

"""
the harness method to create a Planet and Moon tandem
and demonstrate a few methods
"""
def main():
  Earth = Planet(Point3D(0,0,0),4000,7600000000)
  EarthMoon = Moon(Point3D(0,0,250000),800,"Earth's Moon")

  print(Earth.inhabitants)
  Earth.ThanosWasHere() 
  print(Earth.inhabitants)
  EarthMoon.crashIntoPlanet(Earth)
  print(EarthMoon.centerPoint)

main()