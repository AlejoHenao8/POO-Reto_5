# Definimos la clase trianculo equilatero que hereda de Triangle.py
from .Triangle import Triangle

class Equilateral(Triangle):
   def __init__(self, side:float, angles:list):
      super().__init__(side1 = side, side2 = side, side3 = side, angles = angles)
      self.is_regular = True
      self.side = side

   def center(self):
      self.center_point = [self.side / 3, self.side / 3]
      return self.center_point
   
   def compute_area(self):
      return (3 ** 0.5 / 4) * self.side ** 2
   
   def compute_perimeter(self):
      return 3 * self.side