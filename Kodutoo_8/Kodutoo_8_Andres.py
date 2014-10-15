'''
Kodutoo 8
14.10.2014
Andres Liiver
'''

import unittest
from Roman_numerals import convert

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(convert("I"), 1)

    def test_2(self):
        self.assertEqual(convert("IV"), 4)

    def test_3(self):
        self.assertEqual(convert("VI"), 6)

    def test_4(self): # initially fails
        self.assertEqual(convert("XC"), 90)

    def test_5(self): # initially fails
        self.assertEqual(convert("CD"), 400)

    def test_6(self):
        self.assertEqual(convert("MMMMCMXCIX"), 4999)

    def test_7(self):
        self.assertEqual(convert("IIV"), -1)

    def test_8(self):
        self.assertEqual(convert("XXXXX"), -1)

    def test_9(self):
        self.assertEqual(convert("LLCDD"), -1)

    def test_91(self):
        self.assertEqual(convert("blah"), -1)

    def test_92(self):
        self.assertEqual(convert(10), -1) # intially returned None
        
if __name__ == "__main__":
    unittest.main(verbosity=5, exit=False)
