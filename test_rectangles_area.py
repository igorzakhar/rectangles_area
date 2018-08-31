import unittest

from rectangles_area import cover, bounding_box


class RectanglesAreaTest(unittest.TestCase):

    def test_rectangle_area(self):
        rects = [(1, 9, 9, 1)]
        self.assertEqual(cover(bounding_box(rects), rects), 64)

    def test_non_intersecting_rectanles_area(self):
        rects = [(0, 3, 4, 0), (4, 7, 7, 3), (7, 3, 10, 0)]
        self.assertEqual(cover(bounding_box(rects), rects), 33)

    def test_overlapping_rectangles_area(self):
        rects = [(0, 3, 4, 0), (2, 5, 5, 1), (4, 7, 7, 4)]
        self.assertEqual(cover(bounding_box(rects), rects), 28)

    def test_multiple_overlapping_rectangles_area(self):
        rects = [(0, 3, 4, 0), (2, 5, 5, 1), (3, 3, 6, 0)]
        self.assertEqual(cover(bounding_box(rects), rects), 24)


if __name__ == '__main__':
    unittest.main()
