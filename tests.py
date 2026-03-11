import unittest
from main import convex_hull_jarvis


class TestConvexHull(unittest.TestCase):
    
    # def test_example_from_prompt(self):
    #     exit(1)

    # def test_square_with_inner_points(self):
    #     exit(1)

    # def test_duplicates(self):
    #     exit(1)

    # def test_all_collinear(self):
    #     exit(1)

    # def test_two_points(self):
    #     exit(1)

    # def test_single_point(self):
    #    exit(1)

    # def test_triangle(self):
    #     exit(1)

    # def test_collinear_on_edges(self):
    #     exit(1)

    def test_square(self):
        points = [
            (0,0),
            (0,1),
            (1,1),
            (1,0)
        ]

        hull = convex_hull_jarvis(points)

        expected = [
            (0,0),
            (1,0),
            (1,1),
            (0,1)
        ]

        self.assertEqual(set(hull), set(expected)) # doesn't really matter the order just that the points are the same

    def test_triangle(self):
        points = [
            (0,0),
            (2,0),
            (1,2)
        ]

        hull = convex_hull_jarvis(points)

        self.assertEqual(set(hull), set(points))

    def test_complex_shape(self):
        points = [
            (0,3),
            (2,2),
            (1,1),
            (2,1),
            (3,0),
            (0,0),
            (3,3)
        ]

        hull = convex_hull_jarvis(points)

        expected = [
            (0,0),
            (3,0),
            (3,3),
            (0,3)
        ]

        self.assertEqual(set(hull), set(expected))

if __name__ == "__main__":
    unittest.main()