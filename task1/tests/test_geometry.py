import unittest
from task1.src.geometry import Circle, Triangle, calculate_area

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=5)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_non_right_triangle(self):
        triangle = Triangle(2, 3, 4)
        self.assertFalse(triangle.is_right_triangle())

    def test_calculate_area(self):
        circle = Circle(5)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)

    def test_calculate_area_invalid_object(self):
        with self.assertRaises(TypeError):
            calculate_area("Не является фигурой")


if __name__ == '__main__':
    unittest.main()