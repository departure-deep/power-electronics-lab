import unittest

from sim import BuckConverter


class BuckConverterTests(unittest.TestCase):
    def setUp(self):
        self.buck = BuckConverter(12.0, 0.5, 100e3, 47e-6, 100e-6, 10.0)

    def test_ideal_output_voltage(self):
        self.assertAlmostEqual(self.buck.vout, 6.0)

    def test_load_current(self):
        self.assertAlmostEqual(self.buck.i_load, 0.6)

    def test_invalid_duty_is_rejected(self):
        with self.assertRaises(ValueError):
            BuckConverter(12.0, 1.0, 100e3, 47e-6, 100e-6, 10.0)
