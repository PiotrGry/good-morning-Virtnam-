from animals import Animal


class Cat(Animal):
    siersc = ""
    karma = ""
    imie = ""
    wlasciciel = ""

    def __init__(self, siersc, karma, imie, wlasciciel, waga, kolor, dlugosc, rok_ur, plec):
        super().__init__(waga, kolor, dlugosc, rok_ur, plec)
        self.siersc = siersc
        self.karma = karma
        self.imie = imie
        self.wlasciciel = wlasciciel


    def zmiana_karmy(self, nowa_karma):
        self.karma = nowa_karma


    def zmien_piasek(self):
        return "Zmienilem Piasek"

    def __str__(self):
        super().__str__()
        return super().__str__()+ self.siersc+" "+self.karma+" "+self.imie+" "+self.wlasciciel


# cat1 = Cat("gesta", "whiskas", "Fela", "Piotr" ,5, "rudy", 40, 2005, "kobieta" )
# print(cat1.imie+ " "+ cat1.wlasciciel+ " "+ str(cat1.rok_ur)+ " "+ cat1.plec)
# print(type(cat1))
