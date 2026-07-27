from paquete.TetraLados.Rectangle import Rectangle
from paquete.TetraLados.Square import Square
from paquete.TriLados.Scalene import Scalene
from paquete.TriLados.TriRectangle import TriRectangle
from paquete.TriLados.Equilateral import Equilateral
from paquete.TriLados.Isosceles import Isosceles

if __name__ == "__main__":
   rectangle = Rectangle(width = 5, height = 3, center_point = [0, 0])
   print("-- Rectángulo ---")
   print(f"Es el objeto regular?: {rectangle.is_regular}")
   print(f"El área es: {rectangle.compute_area()}")
   print(f"El perímetro es: {rectangle.compute_perimeter()}")
   print(f"El centro es: {rectangle.center()}")
   print()

   square = Square(side = 7)
   print("-- Cuadrado ---")
   print(f"Es el objeto regular?: {square.is_regular}")
   print(f"El área es: {square.compute_area()}")
   print(f"El perímetro es: {square.compute_perimeter()}")
   print(f"El centro es: {square.center()}")
   print()

   scalene = Scalene(side1 = 5, side2 = 6, side3 = 7, angles = [44.42, 57.12, 78.86])
   print("-- Triángulo Escaleno ---")
   print(f"Es el objeto regular?: {scalene.is_regular}")
   print(f"El área es: {scalene.compute_area()}")
   print(f"El perímetro es: {scalene.compute_perimeter()}")
   print(f"El centro es: {scalene.center()}")
   print()

   tri_rectangle = TriRectangle(hypotenuse = 5, catetcathetusx = 4, catetcathetusy = 3, angles = [90, 53.13, 36.87])
   print("-- Triángulo Rectángulo ---")
   print(f"Es el objeto regular?: {tri_rectangle.is_regular}")
   print(f"El área es: {tri_rectangle.compute_area()}")
   print(f"El perímetro es: {tri_rectangle.compute_perimeter()}")
   print(f"El centro es: {tri_rectangle.center()}")
   print()

   equilateral = Equilateral(side = 6, angles = [60, 60, 60])
   print("-- Triángulo Equilátero ---")
   print(f"Es el objeto regular?: {equilateral.is_regular}")
   print(f"El área es: {equilateral.compute_area()}")
   print(f"El perímetro es: {equilateral.compute_perimeter()}")
   print(f"El centro es: {equilateral.center()}")
   print()

   isosceles = Isosceles(side1 = 5, side2 = 8, angles = [40, 70, 70])
   print("-- Triángulo Isósceles ---")
   print(f"Es el objeto regular?: {isosceles.is_regular}")
   print(f"El área es: {isosceles.compute_area()}")
   print(f"El perímetro es: {isosceles.compute_perimeter()}")
   print(f"El centro es: {isosceles.center()}")