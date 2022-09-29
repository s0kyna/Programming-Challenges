# test for SLAYER
import unittest

from SLAYER import*

class TestCalc(unittest.TestCase):

    def testcalc(self):
        self.assertEqual(calculate(142857),(428571, 428571))
        
        
if __name__ == '__main__':
    unittest.main()
