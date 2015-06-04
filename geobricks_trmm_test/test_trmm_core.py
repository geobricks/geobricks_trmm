import unittest
from geobricks_trmm.core import trmm_core as c


class GeobricksTrmmTest(unittest.TestCase):

    def test_list_years(self):
        out = c.list_years()
        self.assertEqual(len(out), 18)

    def test_list_months(self):
        out = c.list_months(2014)
        self.assertEqual(len(out), 12)