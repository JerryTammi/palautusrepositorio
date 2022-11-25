from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostot = []

    def tavaroita_korissa(self):
        tavaroita_korissa = 0
        for o in self.ostot:
            tavaroita_korissa = tavaroita_korissa + o.lukumaara()
        return tavaroita_korissa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for o in self.ostot:
            hinta = hinta + o.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        loytyyko = False
        for o in self.ostot:
            if o.tuote.nimi == lisattava.nimi:
                o.muuta_lukumaaraa(1)
                loytyyko = True
        if not loytyyko:
            osto = Ostos(lisattava)
            self.ostot.append(osto)
        
    def poista_tuote(self, poistettava: Tuote):
        for o in self.ostot:
            if o.tuote.nimi == poistettava.nimi:
                if o.lukumaara() > 1:
                    o.muuta_lukumaaraa(-1)
                else:
                    self.ostot.remove(o)


    def tyhjenna(self):
        self.ostot = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostot
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
