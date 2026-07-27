# Definimos la clase triangulo isoseles que hereda de Triangle.py
from .Triangle import Triangle

class Isosceles(Triangle):
   def __init__(self, side1:float, side2:float, angles:list):
      super().__init__(side1 = side1, side2 = side2, side3 = side2, angles = angles)
      self.is_regular = False
      self.side1 = side1
      self.side2 = side2

   def center(self):
      self.center_point = [self.side1 / 3, self.side2 / 3]
      return self.center_point
   
   def compute_area(self):
      height = (self.side2**2 - (self.side1 / 2)**2) ** 0.5
      return (self.side1 * height) / 2

   def compute_perimeter(self):
      return self.side1 + 2 * self.side2