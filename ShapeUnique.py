"""
A unique module inside of package *Shape*
"""


class Shape:
    """Superclase para inicializar las formas."""

    def __init__(self, is_regular: bool):
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


class Rectangle(Shape):
    """Rectángulo que hereda de Shape."""

    def __init__(self, width: float, height: float, center_point: list):
        super().__init__(is_regular=False)
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


class Square(Rectangle):
    """Cuadrado que hereda de Rectangle."""

    def __init__(self, side: float):
        super().__init__(width=side, height=side, center_point=[0, 0])
        self.is_regular = True
        self.side = side

    def center(self):
        self.center_point = [self.side / 2, self.side / 2]
        return self.center_point

    def compute_area(self):
        return self.side**2

    def compute_perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    """Triángulo que hereda de Shape."""

    def __init__(self, side1: float, side2: float, side3: float, angles: list):
        super().__init__(is_regular=False)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angles = angles


class Equilateral(Triangle):
    """Triángulo equilátero que hereda de Triangle."""

    def __init__(self, side: float, angles: list):
        super().__init__(side1=side, side2=side, side3=side, angles=angles)
        self.is_regular = True
        self.side = side

    def center(self):
        self.center_point = [self.side / 3, self.side / 3]
        return self.center_point

    def compute_area(self):
        return (3**0.5 / 4) * self.side**2

    def compute_perimeter(self):
        return 3 * self.side


class Isosceles(Triangle):
    """Triángulo isósceles que hereda de Triangle."""

    def __init__(self, side1: float, side2: float, angles: list):
        super().__init__(side1=side1, side2=side2, side3=side2, angles=angles)
        self.is_regular = False
        self.side1 = side1
        self.side2 = side2

    def center(self):
        self.center_point = [self.side1 / 3, self.side2 / 3]
        return self.center_point

    def compute_area(self):
        height = (self.side2**2 - (self.side1 / 2) ** 2) ** 0.5
        return (self.side1 * height) / 2

    def compute_perimeter(self):
        return self.side1 + 2 * self.side2


class Scalene(Triangle):
    """Triángulo escaleno que hereda de Triangle."""

    def __init__(self, side1: float, side2: float, side3: float, angles: list):
        super().__init__(side1=side1, side2=side2, side3=side3, angles=angles)
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


class TriRectangle(Triangle):
    """Triángulo rectángulo que hereda de Triangle."""

    def __init__(
        self,
        hypotenuse: float,
        catetcathetusx: float,
        catetcathetusy: float,
        angles: list,
    ):
        super().__init__(
            side1=hypotenuse,
            side2=catetcathetusx,
            side3=catetcathetusy,
            angles=angles,
        )
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


if __name__ == "__main__":
    rectangle = Rectangle(width=5, height=3, center_point=[0, 0])
    print("-- Rectángulo ---")
    print(f"Es el objeto regular?: {rectangle.is_regular}")
    print(f"El área es: {rectangle.compute_area()}")
    print(f"El perímetro es: {rectangle.compute_perimeter()}")
    print(f"El centro es: {rectangle.center()}")
    print()

    square = Square(side=7)
    print("-- Cuadrado ---")
    print(f"Es el objeto regular?: {square.is_regular}")
    print(f"El área es: {square.compute_area()}")
    print(f"El perímetro es: {square.compute_perimeter()}")
    print(f"El centro es: {square.center()}")
    print()

    scalene = Scalene(side1=5, side2=6, side3=7, angles=[50, 60, 70])
    print("-- Triángulo Escaleno ---")
    print(f"Es el objeto regular?: {scalene.is_regular}")
    print(f"El área es: {scalene.compute_area()}")
    print(f"El perímetro es: {scalene.compute_perimeter()}")
    print(f"El centro es: {scalene.center()}")
    print()

    tri_rectangle = TriRectangle(hypotenuse=5, catetcathetusx=4, catetcathetusy=3, angles=[90, 53.13, 36.87])
    print("-- Triángulo Rectángulo ---")
    print(f"Es el objeto regular?: {tri_rectangle.is_regular}")
    print(f"El área es: {tri_rectangle.compute_area()}")
    print(f"El perímetro es: {tri_rectangle.compute_perimeter()}")
    print(f"El centro es: {tri_rectangle.center()}")
    print()

    equilateral = Equilateral(side=6, angles=[60, 60, 60])
    print("-- Triángulo Equilátero ---")
    print(f"Es el objeto regular?: {equilateral.is_regular}")
    print(f"El área es: {equilateral.compute_area()}")
    print(f"El perímetro es: {equilateral.compute_perimeter()}")
    print(f"El centro es: {equilateral.center()}")
    print()

    isosceles = Isosceles(side1=5, side2=8, angles=[40, 70, 70])
    print("-- Triángulo Isósceles ---")
    print(f"Es el objeto regular?: {isosceles.is_regular}")
    print(f"El área es: {isosceles.compute_area()}")
    print(f"El perímetro es: {isosceles.compute_perimeter()}")
    print(f"El centro es: {isosceles.center()}")
