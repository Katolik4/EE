from collections import namedtuple

Uczen = namedtuple('Uczen', ['imie', 'nazwisko', 'grupa'])


class Db:
    def __init__(self):
        self.data = {}
        self.data['uczniowie'] = []

    @property
    def uczeniowie(self):
        return self.data['uczniowie']

    def dodaj_ucznia(self, uczen:Uczen):
        self.data['uczniowie'].append(uczen)

    def __call__(self):
        return self

Db = Db()

