# Definimos la clase triangulo que hereda de Shape.py
from ..Shape import Shape

class Triangle(Shape):
   def __init__(self, side1:float, side2:float, side3:float, angles:list):
      super().__init__(is_regular = False)
      self.side1 = side1
      self.side2 = side2
      self.side3 = side3
      self.angles = angles