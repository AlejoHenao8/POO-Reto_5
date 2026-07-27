# Superclase para inicializar las formas
class Shape:
   def __init__(self, is_regular:bool):
      self.is_regular = is_regular

   def vertices(self):
      pass

   def edges(self):
      pass

   def inner_angles(self):
      pass

   def compute_area(self):
      pass

   def compute_perimeter(self):
      pass

   def compute_inner_angles(self):
      pass

if __name__ == "__main__":
   object = Shape(is_regular = True)
   print(f"el objeto es regular?: {object.is_regular}")