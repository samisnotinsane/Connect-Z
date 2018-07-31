# Test suit for connectz.py
import unittest

class TestStringMethods(unittest.TestCase):
    
    def setup(self):
        

    def test_bottom_row(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()