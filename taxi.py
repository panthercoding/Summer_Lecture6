import numpy as np 

class Point():

  def __init__(self,x,y,z):
    """ delete the below and finish the constructor method """
    pass
  
  def taxicab(self,other):
    """ computes and returns the Taxicab distance between two 2D points """
    return(0)

  """ prewritten method to print out a 3D coordinate """
  def __str__(self):
    return "<{},{}>".format(self.x,self.y)

def main():
  """ create two points and compute and print out the taxicab distance """