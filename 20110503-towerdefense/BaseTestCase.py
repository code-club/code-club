import unittest

from base import Base

class BaseTestCase(unittest.TestCase):
    def test_la_base_peut_perdre_des_pv(self):
        b = Base()
        self.assertEqual(b.pv, 20)
        before = b.pv
        b.attaquer()
        after = b.pv
        self.assertEqual(before - 1, after)
        b.attaquer(25)
        self.assertEqual(b.pv, 0)

   