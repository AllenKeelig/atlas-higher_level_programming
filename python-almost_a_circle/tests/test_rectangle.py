import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_init(self):
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r1.id, 99)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_rectangle_default_id(self):
        r2 = Rectangle(5, 10)
        r3 = Rectangle(15, 20)
        self.assertEqual(r2.id + 1, r3.id)

    def test_rectangle_getters_setters(self):
        r4 = Rectangle(1, 2, 3, 4)
        r4.width = 5
        r4.height = 6
        r4.x = 7
        r4.y = 8
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 6)
        self.assertEqual(r4.x, 7)
        self.assertEqual(r4.y, 8)
    
    def test_rectangle_minimal_parameters(self):
        r5 = Rectangle(1, 2)
        self.assertEqual(r5.width, 1)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)
    
    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
    
    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
    
    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3", 4)
    
    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
    
    def test_invalid_width_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
    
    def test_invalid_height_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
    
    def test_invalid_x_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4)
    
    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

if __name__ == '__main__':
    unittest.main()
