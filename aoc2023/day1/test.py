import unittest
from day1 import Calibration

class TestCalibrations(unittest.TestCase):

    def test_sum_empty(self):
        self.calibration = Calibration([])
        self.assertEqual(self.calibration.get_sum(), 0, 'The sum is wrong.')

    def test_sum_nonempty(self):
        self.calibration = Calibration(["1","2","3"])
        self.assertEqual(self.calibration.get_sum(), 13, 'The sum is wrong.')

if __name__ == '__main__':
    unittest.main()