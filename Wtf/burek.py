from cat import Cat

class Burek(Cat):
    zabawki = []
    poziom_wyspania = 0
    poziom_wyglaskania = 0
    poziom_gniewu = 0
    zaglada_swiata = False

    def __init__(self, siersc, karma, imie, wlasciciel, waga, kolor, dlugosc, rok_ur, plec, zabawki, poziom_wyspania,\
                    poziom_wyglaskania, poziom_gniewu, zaglada_swiata):
        super().__init__(siersc, karma, imie, wlasciciel, waga, kolor, dlugosc, rok_ur, plec)
        self.zabawki = zabawki
        self.poziom_wyspania = poziom_wyspania
        self.poziom_gniewu = poziom_gniewu
        self.poziom_wyglaskania = poziom_wyglaskania
        self.zaglada_swiata = zaglada_swiata

        def __str__ (self):
            return self.zabawki+" "+str(self.poziom_wyspania)+" "+str(self.poziom_wyglaskania)+" "+str(self.poziom_gniewu)
burek1 = Burek(["drapak", "pileczka"],10, 50, 5, True, "gesta", "whiskas", "Fela", "Piotr" ,5, "rudy", 40, 2005, "kobieta")
print(burek1)
