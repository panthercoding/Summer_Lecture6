import numpy as np 

class Point():

  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def taxicab(self,other):
    """ computes and returns the Taxicab distance between two 2D points """
    diff_x = abs(self.x - other.x)
    diff_y = abs(self.y - other.y)

    return diff_x + diff_y

  """ prewritten method to print out a 3D coordinate """
  def __str__(self):
    return "<{},{}>".format(self.x,self.y)

def main():
  """ create two points and compute and print out the taxicab distance """
  school = Point(-5,-4)
  mcdonalds = Point(8,3)

  print(school.taxicab(mcdonalds))

main()