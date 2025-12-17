import unittest

def area(a, b):
    """Вычисляет площадь прямоугольника по двум сторонам"""
    return a * b 

def perimeter(a, b): 
    """Вычисляет периметр прямоугольника по двум сторонам"""
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):

    def test_area_zero_side(self):
        """При нулевой стороне площадь должна быть равна 0"""
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        """Площадь квадрата со стороной 10 равна 100"""
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_regular(self):
        """Площадь прямоугольника со сторонами 3 и 4 равна 12"""
        res = area(3, 4)
        self.assertEqual(res, 12)


    def test_perimeter_regular(self):
        """Периметр прямоугольника со сторонами 3 и 4 равен 14"""
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_zero_side(self):
        """Периметр прмоугольника со сторонами 0 и 5 должен быть равен 10"""
        res = perimeter(0, 5)
        self.assertEqual(res, 10)

if __name__ == "__main__":
    unittest.main()