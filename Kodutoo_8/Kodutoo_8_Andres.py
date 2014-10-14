'''
Kodutoo 8
14.10.2014
Andres Liiver
'''

import unittest
from Roman_numerals import convert
import re

class Test(unittest.TestCase):
    def test_1(self):
        file = open("roman_numerals.txt")

        for line in file:
            test = re.findall(r'[^,;\s]+', line)
            print(test)
            self.assertEqual(convert(test[0]), int(test[1]))

        file.close()
        
if __name__ == "__main__":
    unittest.main(verbosity=5, exit=False)
