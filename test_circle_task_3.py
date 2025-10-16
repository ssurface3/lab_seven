import unittest
import math
from circle import compute_area

class TestComputeArea(unittest.TestCase):

    def test_valid_input(self):
        
        radius = 5.0
        expected_area = math.pi * radius ** 2
        self.assertAlmostEqual(compute_area(radius), expected_area, places=5)

        radius = 10.0
        expected_area = math.pi * radius ** 2
        self.assertAlmostEqual(compute_area(radius), expected_area, places=5)

    def test_invalid_input(self):
       
        radius = -1.0
        with self.assertRaises(ValueError):
            compute_area(radius)

    def test_boundary(self):
        radius = 0.0
        expected_area = math.pi * radius ** 2
        self.assertAlmostEqual(compute_area(radius), expected_area, places=5)

if __name__ == '__main__':
    unittest.main()

