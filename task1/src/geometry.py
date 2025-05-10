import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом!")
        self.radius = radius

    def area(self):
        """Вычисляет площадь круга."""
        return math.pi * self.radius ** 2


class Triangle:
    def __init__(self, a, b, c):
        # Проверяем, что стороны треугольника положительные и могут образовать треугольник
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными числами!")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Такого треугольника не существует!")

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """Вычисляет площадь треугольника по формуле Герона."""
        s = (self.a + self.b + self.c) / 2  # Полупериметр
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self):
        """Проверяет, является ли треугольник прямоугольным."""
        sides = sorted([self.a, self.b, self.c])  # Сортируем стороны
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)


def calculate_area(shape):
    """
    Вычисляет площадь фигуры без знания её типа.
    Принимает объект, у которого есть метод area().
    """
    if not hasattr(shape, 'area'):
        raise TypeError("Переданный объект не имеет метода area()!")
    return shape.area()