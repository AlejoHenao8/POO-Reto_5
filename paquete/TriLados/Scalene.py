# Definimnos la clase triangulo escaleno que hereda de Triangle.py
from .Triangle import Triangle

class Scalene(Triangle):
   def __init__(self, side1:float, side2:float, side3:float, angles:list):
      super().__init__(side1 = side1, side2 = side2, side3 = side3, angles = angles)
      self.is_regular = False
      self.side1 = side1
      self.side2 = side2
      self.side3 = side3

   def center(self):
      self.center_point = [self.side1 / 3, self.side2 / 3]
      return self.center_point
   
   def compute_area(self):
      s = (self.side1 + self.side2 + self.side3) / 2
      return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

   def compute_perimeter(self):
      return self.side1 + self.side2 + self.side3