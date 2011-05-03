import unittest

from ennemi import Ennemi

class EnnemiTestCase(unittest.TestCase):
    def test_ennemi_perd_pv(self):
        e = Ennemi(force=3, pv=25)
        e.attaquer()
        self.assertEqual(e.pv, 24)
        e.attaquer(1000)
        self.assertEqual(e.pv, 0)

    def test_les_ennemis_vont_de_gauche_droite(self):
        e = Ennemi()
        e.avance()
        self.assertEqual(e.x, 1)