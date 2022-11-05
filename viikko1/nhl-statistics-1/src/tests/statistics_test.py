import unittest
from statistics import SortBy, Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_loytyyko_pelaaja(self):
        pelaaja = self.statistics.search("Kurri")
        self.assertAlmostEqual(pelaaja.name,"Kurri")

    def test_ei_loydy_pelaaja(self):
        pelaaja = self.statistics.search("Motivaatio")
        self.assertAlmostEqual(pelaaja, None)

    def test_montako_samassa_tiimissa(self):
        lista = self.statistics.team("EDM")
        self.assertAlmostEqual(len(lista), 3)

    def test_jarjestetty_lista_pisteiden_mukaan(self):
        lista = self.statistics.top(3)
        paras = lista[0]
        self.assertAlmostEqual(paras.name, "Gretzky")

    def test_jarjestetty_lista_maalien_mukaan(self):
        lista = self.statistics.top(3, SortBy.GOALS)
        paras = lista[0]
        self.assertAlmostEqual(paras.name, "Lemieux")

    def test_jarjestetty_lista_syottojen_mukaan(self):
        lista = self.statistics.top(3, SortBy.ASSISTS)
        paras = lista[0]
        self.assertAlmostEqual(paras.name, "Gretzky")