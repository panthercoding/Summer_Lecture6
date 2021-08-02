import numpy as np 

""" helper function to calculate arc cosine given radians """
def arccosine(theta):
  return np.arccos(theta)

class Point3D():

  def __init__(self,x,y,z):
    """ delete the below and finish the constructor method """
    pass

  def EuclideanDistance(self,other):
    """ calculate the Euclidean distance between two points
    and returns it (delete the below) """
    return(0)

  def greatCircleDistance(self,other):
    """ calculate the great-circle distance between two points 
    located on a sphere centered at (0,0,0); formula on handout.
    Return this great-circle distance.
    
    make sure to calculate the distance of each point to origin, 
    and set r equal to the larger distance should they differ
    (approximates distance for non-spheroid planet)"""
    return(0)
  
  """ prewritten method to print out a 3D coordinate """
  def __str__(self):
    return "<{},{},{}>".format(self.x,self.y,self.z)
  
def main():
  Point1 = Point3D(-40,30,-20)
  Point2 = Point3D(20,-30,40)

  distance_Euclid = Point1.EuclideanDisatnce(Point2)
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