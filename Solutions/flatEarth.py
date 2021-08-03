import numpy as np 

""" helper function to calculate arc cosine given radians """
def arccosine(theta):
  return np.arccos(theta)

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
  
def main():
  Point1 = Point3D(0,0,4000) #north Pole
  Point2 = Point3D(0,0,-4000) #$south Pole

  distance_Euclid = Point1.EuclideanDistance(Point2)
  distance_GC = Point1.greatCircleDistance(Point2)
  print("The Euclidean distance between {} and {} is equal to {}".format(Point1,Point2,distance_Euclid))
  print("The great circle distance between {} and {} is equal to {}".format(Point1,Point2,distance_GC))

  """ create some new points and try looking at a real life globe to model and estimate,
  to the best of your mathematical dexterity, the 3D locations of certain cities
  on the earth and calculate the great-circle (NOT EUCLIDEAN) distance and print it out 
  
  for reference, the radius of the aerth is approximately 4000 miles and you can presume
  that the Earth has a fullty spheroid shape (actually an oblate spheroid)
  
  if you are a flat earther, ignore this exercise all together"""
  
main()