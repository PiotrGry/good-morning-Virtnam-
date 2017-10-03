import datetime

class Animal():
    waga = 0
    kolor = ""
    dlugosc = 0
    rok_ur = 0
    plec = ""
    """
    konstruktor
            |
            V
    """
    def __init__(self, waga, kolor, dlugosc, rok_ur, plec):
        self.waga = waga
        self.kolor = kolor
        self.dlugosc = dlugosc
        self. rok_ur = rok_ur
        self.plec = plec

    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor

    def aktualny_wiek(self):
        aktualny_rok = datatime.data.today().year
        return aktualny_rok - self.rok_ur

    def bmi_zwierzecia(self):
        return self.waga/(self.dlugosc**2)


    def __str__(self):
        return str(self.waga)+" " +self.kolor+ " "+str(self.dlugosc)+" "+str(self.rok_ur)+ " "+self.plec
