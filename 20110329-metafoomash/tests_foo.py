import unittest
from foo import Foo, K

class FooTests(unittest.TestCase):
    def setUp(self):
        Foo.clear()
    
    def test_on_peu_voter_entre_deux_foo(self):
        foo1 = Foo('machin')
        foo2 = Foo('truc')

        foo1.a_vaincu(foo2)

        self.assertEqual(1500.+K/2, foo1.score)
        self.assertEqual(1500.-K/2, foo2.score)

    def test_on_peut_renvoyer_du_hteumeuleu(self):
        foo = Foo('superFooMash')
        self.assertIsInstance(foo.__html__(), str)

    def test_on_peut_ajouter_des_foos(self):
        foo = Foo('ciblout')
        Foo.ajouter(foo)
        self.assertIn(foo, foo.get_liste())

    def test_on_peut_avoir_plein_de_foo(self):
        liste_foo = Foo.get_liste()
        for foo in liste_foo:
            self.assertIsInstance(foo.name, str)
            self.assertIsInstance(foo.score, float)
            self.assertIsInstance(foo.__html__(), str)

    def test_clear(self):
        foo = Foo('ciclout')
        Foo.ajouter(foo)
        Foo.clear()
        self.assertEqual(Foo.get_liste(), [])

    def test_on_peut_avoir_deux_foo_aleatoires(self):
        foo1 = Foo('ciblout')
        foo2 = Foo('remram')
        Foo.ajouter(foo1)
        Foo.ajouter(foo2)

        foos = Foo.get_two_foos()
        self.assertEqual(len(foos),2)
        self.assertIn(foo1,foos)
        self.assertIn(foo2,foos)

    def test_cas_foireux_pour_deux_foos(self):
        self.assertRaises(Foo.NotEnoughFoos,
                          Foo.get_two_foos)
        Foo.ajouter(Foo('chose'))
        self.assertRaises(Foo.NotEnoughFoos,
                          Foo.get_two_foos)

    def test_on_peut_classer(self):
        foo1 = Foo('ciblout')
        foo2 = Foo('remram')
        foo3 = Foo('remram')
        Foo.ajouter(foo1)
        Foo.ajouter(foo2)
        Foo.ajouter(foo3)
        foo1.a_vaincu(foo2)

        foos = Foo.get_sorted_list(2)

        self.assertEqual(len(foos), 2)
        self.assertEqual(foo1, foos[0])
        self.assertEqual(foo3, foos[1])

    def test_get_by_name(self):
        Foo.ajouter(Foo('ciblout'))
        Foo.ajouter(Foo('remram'))
        Foo.ajouter(Foo('lily'))
        foo = Foo.get_by_name('remram')
        self.assertEqual('remram',foo.name)