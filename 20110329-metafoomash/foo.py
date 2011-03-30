import random

K = 25

class Foo(object):
    class NotEnoughFoos(Exception):
        pass
    
    _foo_liste = []

    def __init__(self,name):
        self.name = name
        self.score = 1500.

    def a_vaincu(self,autre):
        ra = self.score
        rb = autre.score
        qa = 10**(ra/400)
        qb = 10**(rb/400)
        ea = qa / (qa + qb)
        eb = qb / (qa + qb)
        self.score += K*(1-ea)
        autre.score += K*(-eb)
        

    def __html__(self):
        return self.name

    def __repr__(self):
        return "<Foo: %s>"%(self.name)

    @staticmethod
    def ajouter(foo):
        Foo._foo_liste.append(foo)

    @staticmethod
    def get_liste():
        return Foo._foo_liste

    @staticmethod
    def get_two_foos():
        if len(Foo.get_liste()) < 2:
            raise Foo.NotEnoughFoos()
        foo1 = random.choice(Foo._foo_liste)
        foo2 = foo1
        while(foo1 == foo2):
            foo2 = random.choice(Foo._foo_liste)

        return foo1, foo2

    @staticmethod
    def clear():
        Foo._foo_liste = []

    @staticmethod
    def get_sorted_list(length):
        list = sorted(Foo.get_liste(), key = lambda x:x.score, reverse = True)
        return list[:length]

    @staticmethod
    def get_by_name(name):
        for foo in Foo.get_liste():
            if foo.name == name :
                return foo
        
        