# Define la clase cuadrado que hereda de Rectangle.py
from .Rectangle import Rectangle

class Square(Rectangle):
   def __init__(self, side:float):
      super().__init__(width = side, height = side, center_point = [0, 0])
      self.is_regular = True
      self.side = side

   def center(self):
         self.center_point = [self.side / 2, self.side / 2]
         return self.center_point

   def compute_area(self):
         return self.side ** 2
      
   def compute_perimeter(self):
         return 4 * self.side
   
