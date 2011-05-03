import unittest

from ennemi import Ennemi
from Carte import Carte

class CarteTestCase(unittest.TestCase):

    def test_ta_soeur(self) :
        pass

    def test_les_ennemis_avancent(self):
        e1 = Ennemi(vitesse=8)
        e2 = Ennemi(vitesse=3)
        c = Carte()
        c.ajouter(e1)
        c.ajouter(e2)
        c.tick()
        self.assertEqual(e1.x, 8)
        self.assertEqual(e2.x, 3)

    def test_ajout_ennemi(self):
        e = Ennemi()
        carte = Carte()
        carte.ajouter(e)
        self.assertIn(e, carte.ennemis)

    def test_quand_un_ennemiszz_atteinxxx_la_base_il_la_poutre(self):
        e = Ennemi(force=1, vitesse=1)
        c = Carte(3)
        c.ajouter(e)
        for i in range(4):
            c.tick()
        self.assertNotIn(e, c.ennemis)
        self.assertEqual(c.base.pv, 19)
        