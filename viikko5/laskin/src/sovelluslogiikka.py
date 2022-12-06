class Sovelluslogiikka:
    def __init__(self):
        self.tulos = 0
        self.vanha = 0

    def suorita(self, luku):
        self.vanha = self.tulos
        self.tulos = self.laske(luku)
        return self.tulos

    def laske(self, luku):
        return luku

class Summa(Sovelluslogiikka):
    def __init__(self, sovellulogiikka, lue_syote):
        self.tulos = sovellulogiikka.tulos
        self.lue_syote = lue_syote

    def laske(self, luku):
        return int(self.lue_syote()) + luku

class Erotus(Sovelluslogiikka):
    def __init__(self, sovellulogiikka, lue_syote):
        self.tulos = sovellulogiikka.tulos
        self.lue_syote = lue_syote

    def laske(self, luku):
        return luku - int(self.lue_syote())

class Nollaus(Sovelluslogiikka):
    def __init__(self, sovellulogiikka, lue_syote):
        super().__init__()
        self.tulos = sovellulogiikka.tulos
        self.lue_syote = lue_syote

    def laske(self, luku):
        return 0

class Kumoa(Sovelluslogiikka):
    def __init__(self, sovellulogiikka, lue_syote):
        super().__init__()
        self.vanha = sovellulogiikka.vanha
        self.lue_syote = lue_syote()

    def laske(self, luku):
        return self.vanha
