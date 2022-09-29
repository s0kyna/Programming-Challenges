# test for 3 - the 99 trick
import unittest

from THE_99_TRICK import*

class TestCalc(unittest.TestCase):

    def testcalc(self):
        self.assertEqual(calculation(15,88),15)
        
        
if __name__ == '__main__':
    unittest.main()
