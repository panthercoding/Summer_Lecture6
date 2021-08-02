class Rectangle():

  def __init__(self,length,width):
    """delete the below and finish the constructor method"""
    pass
  
  def area(self):
    """delete the below and finish this method, which should
    compute and return the area of the rectangle """
    return(0)

  def perimeter(self):
    """delete the below and finish this method, which should
    compute and return the perimeter of the rectangle """
    return(0)

def test_rectangle():
  """ here, create a rectangle data object in Python with length 5 and width 3 and compute its area and perimeter, and print both values out with a description."""
  return(0)

class Square(Rectangle):

  def __init__(self,length,width):
    """delete the below and finish the constructor
     Inside the constructor method, we can use super( ).__init__(x,x)
     to form our square, which is essentially a rectangle with equal sides of length x.

     Note that due to inheritance, we can use the area and perimeter formulas
     from the Rectangle class. 
     """
    return(0)

def test_square():
  """ here, create a Square data object in Python with length 10 and compute its area and perimeter, and print both values out with a description."""
  return(0)

def main():
  test_rectangle()
  test_square()
  print("Tests complete!")