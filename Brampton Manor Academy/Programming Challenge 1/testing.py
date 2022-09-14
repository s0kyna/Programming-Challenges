# Test
import unittest

from ROD_CONVERSIONS import*

class TestCalc(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(meters(10),50.292)
        
    def test_feet(self):
        self.assertEqual(feet(10),165.0)
        
    def test_miles(self):
        self.assertEqual(miles(10),0.03125007767159208)
        
    def test_furlongs(self):
        self.assertEqual(furlongs(10),0.25)
        
    def test_minutes(self):
        self.assertEqual(minutes(10),0.6048402129985564)
        
if __name__ == '__main__':
    unittest.main()
