class AttaquableMixin:
    def attaquer(self, force=1):
        self.pv = max(0, self.pv - force)


class Base(AttaquableMixin):
    def __init__(self):
        self.pv = 20