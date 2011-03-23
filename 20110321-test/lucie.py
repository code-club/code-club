import unittest
from nose.tools import *

PIECES = [1, 2, 5, 10, 20, 50, 100, 200]
PIECES.reverse()

def rendre(montant):
    comptoir = []
    for piece in PIECES:
        while montant >= piece:
            comptoir.append(piece)
            montant = montant - piece

    return comptoir

class Test(unittest.TestCase):
    def test_une_piece_exacte_doit_etre_rendue(self):
        for piece in [1, 2, 5, 10, 20, 50, 100, 200]:
            assert_equal(rendre(piece), [piece])

    def test_un_double_renvoit_deux_pieces(self):
        assert_equal(rendre(40), [20, 20])

    def test_piece_dans_ordre_decroissant(self):
        assert_equal(PIECES[0], 200)
