# Definimos la clase rectangulo que hereda de Shape.py
from ..Shape import Shape

class Rectangle(Shape):
   def __init__(self, width:float, height:float, center_point:list):
      super().__init__(is_regular = False)
      self.width = width
      self.height = height
      self.center_point = center_point

   def center(self):
      self.center_point = [self.width / 2, self.height / 2]
      return self.center_point

   def compute_area(self):
      return self.width * self.height

   def compute_perimeter(self):
      return 2 * (self.width + self.height)
