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
        out = c.list_days(2014, 1)
        self.assertEqual(len(out), 31)

    def test_list_layers(self):
        out = c.list_layers(2014, 1, 5)
        self.assertEqual(len(out), 8)

    def test_list_layers_subset(self):
        out = c.list_layers_subset(2014, 1, 5, 8)
        self.assertEqual(len(out), 64)

    def test_list_layers_month_subset(self):
        out = c.list_layers_month_subset(2014, 2)
        self.assertEqual(len(out), 448)
