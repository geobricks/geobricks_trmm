import unittest
from geobricks_trmm.core import trmm_core as c


class GeobricksTrmmTest(unittest.TestCase):

    def test_list_years(self):
        out = c.list_years()
        self.assertEqual(len(out), 18)

    def test_list_months(self):
        out = c.list_months(2014)
        self.assertEqual(len(out), 12)

    def test_list_days(self):
        out = c.list_days(2014, 01)
        self.assertEqual(len(out), 31)

    def test_list_layers(self):
        out = c.list_layers(2014, 01, 05)
        self.assertEqual(len(out), 8)