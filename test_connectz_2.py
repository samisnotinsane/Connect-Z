import unittest
from connectz_2 import *

class TokenTest(unittest.TestCase):
    def setUp(self):
        self.token_1 = Token()

    def tearDown(self):
        self.token_1 = None

    def test_colour_empty(self):
        self.assertEqual(self.token_1.get_colour(), None)

    def test_x_pos_init(self):
        self.assertEqual(self.token_1.get_x_pos(), -1)

    def test_y_pos_init(self):
        self.assertEqual(self.token_1.get_y_pos(), -1)

    def test_colour_r(self):
        self.token_1.set_colour('r')
        self.assertEqual(self.token_1.get_colour(), 'r')
    
    def test_x_pos(self):
        self.token_1.set_x_pos(2)
        self.assertEqual(self.token_1.get_x_pos(), 2)
    
    def test_y_pos(self):
        self.token_1.set_y_pos(4)
        self.assertEqual(self.token_1.get_y_pos(), 4)

class GridSmallTest(unittest.TestCase):
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

    def test_get_col(self):
        self.grid.set_item(0,0,1)
        self.grid.set_item(1,0,4)
        self.grid.set_item(2,0,7)
        self.assertEqual(self.grid.get_col(0), [1,4,7])

class BoardTest(unittest.TestCase):
    def setUp(self):
        x = 7 # Width
        y = 3 # Height
        z = 3 # Line length
        self.board = Board(x = x, y = y, z = z)
    
    def tearDown(self):
        self.board = None

    def test_get_width(self):
        self.assertEqual(self.board.get_width(), 7)

    def test_get_height(self):
        self.assertEqual(self.board.get_height(), 3)

    def test_get_line_length(self):
        self.assertEqual(self.board.get_line_length(), 3)

    def test_get_next_empty_row_no_1(self):
        grid = self.board.get_grid()
        grid.set_item(row = 2, col = 0, val = 15)
        grid.set_item(row = 1, col = 0, val = 8)
        row_no = self.board.get_next_empty_row_no(column_no = 0)
        self.assertEqual(row_no, 0)

    def test_get_next_empty_row_no_2(self):
        grid = self.board.get_grid()
        row_no = self.board.get_next_empty_row_no(column_no = 1)
        self.assertEqual(row_no, 2)

    def test_get_next_empty_row_no_3(self):
        grid = self.board.get_grid()
        grid.set_item(row = 2, col = 2, val = 17)
        row_no = self.board.get_next_empty_row_no(column_no = 2)
        self.assertEqual(row_no, 1)

    def test_drop_token(self):
        self.board.drop_token(column_no = 0, token = 1)
        row_no = self.board.get_next_empty_row_no(column_no = 0)
        self.board.drop_token(column_no = 0, token = 2)
        row_no = self.board.get_next_empty_row_no(column_no = 0)
        self.board.drop_token(column_no = 0, token = 1)
        row_no = self.board.get_next_empty_row_no(column_no = 0)
        self.assertEqual(self.board.get_next_empty_row_no(column_no = 0), -1)

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(GridTestSmall('test_num_rows'))
#     return suite
