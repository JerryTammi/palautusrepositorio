import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.mehu = Tuote("Mehu", 3)

    # step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        #asd
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # step 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), self.maito.hinta())

    # step 4
    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_tuotetta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_2x_tuotteet(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)

        hinta = self.maito.hinta() + self.mehu.hinta()

        self.assertEqual(self.kori.hinta(), hinta)

    # step 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_2x_tuotteet(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        hinta = self.maito.hinta() * 2

        self.assertEqual(self.kori.hinta(), hinta)

    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
