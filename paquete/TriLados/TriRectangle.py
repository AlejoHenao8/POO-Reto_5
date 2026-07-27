# Definimos la clase triangulo rectángulo que hereda de Triangle.py
from .Triangle import Triangle

class TriRectangle(Triangle):
   def __init__(self, hypotenuse:float, catetcathetusx:float, catetcathetusy:float, angles:list):
      super().__init__(side1 = hypotenuse, side2 = catetcathetusx, side3 = catetcathetusy, angles = angles)
      self.is_regular = False
      self.hypotenuse = hypotenuse
      self.catetcathetusx = catetcathetusx
      self.catetcathetusy = catetcathetusy

   def center(self):
      self.center_point = [self.catetcathetusx / 3, self.catetcathetusy / 3]
      return self.center_point
   
   def compute_area(self):
      return (self.catetcathetusx * self.catetcathetusy) / 2
   
   def compute_perimeter(self):
      return self.hypotenuse + self.catetcathetusx + self.catetcathetusy