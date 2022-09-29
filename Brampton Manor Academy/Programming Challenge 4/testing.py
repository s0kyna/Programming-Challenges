# test WINDCHILL
import unittest

from WINDCHILL import*

class TestCalc(unittest.TestCase):

    def testcalc(self):
        self.assertEqual(wind_chill(10,15),-6.5895344209562525)

        
if __name__ == '__main__':
    unittest.main()
