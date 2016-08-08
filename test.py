#!/usr/bin/python3

import unittest
from kmeans import Point

class PointTestCase(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(0.0, 0.0)
        self.p2 = Point(0.0, 10.0)
        self.p3 = Point(-3.0, -4.0)
        
    def test_distance_to(self):
        self.assertAlmostEqual(self.p1.distance_to(self.p1), 0.0)
        self.assertAlmostEqual(self.p1.distance_to(self.p2), 10.0)
        self.assertAlmostEqual(self.p1.distance_to(self.p3), 5.0)

if __name__ == '__main__':
    unittest.main()
