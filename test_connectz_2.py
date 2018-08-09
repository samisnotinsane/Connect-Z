import unittest
from connectz_2 import *

class GridTestSmall(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(3,3)
    
    def tearDown(self):
        self.grid = None

    def test_num_rows(self):
        self.assertEqual(self.grid.num_rows(), 3)
    
    def test_num_cols(self):
        self.assertEqual(self.grid.num_cols(), 3)
    
    def test_get_item_init(self):
        self.assertEqual(self.grid.get_item(0,0), 0)

    def test_set_get_item(self):
        self.grid.set_item(0,0,1)
        self.assertEqual(self.grid.get_item(0,0), 1)

    def test_get_set_item_2(self):
        self.grid.set_item(2,1,25)
        self.assertEqual(self.grid.get_item(2,1), 25)

class BoardTest(unittest.TestCase):
    def setUp(self):
        x = 7 # Width
        y = 6 # Height
        z = 4 # Line length
        self.board = Board(x = x, y = y, z = z)
    
    def tearDown(self):
        self.board = None

    def test_get_width(self):
        self.assertEqual(self.board.get_width(), 7)

    def test_get_height(self):
        self.assertEqual(self.board.get_height(), 6)

    def test_line_length(self):
        self.assertEqual(self.board.get_line_length(), 4)

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(GridTestSmall('test_num_rows'))
#     return suite
