from abc import ABC, abstractmethod
from datetime import datetime


class Szoba(ABC):
    def __init__(self, szobaszam):
        self.szobaszam = szobaszam

    @abstractmethod
    def ar(self):
        pass


class EgyagyasSzoba(Szoba):
    def ar(self):
        return 5000


class KetagyasSzoba(Szoba):
    def ar(self):
        return 8000


class Szalloda:
    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak
        self.foglalasok = []


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class SzallodaKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda

    def foglalas(self, szoba, datum):
        if datum > datetime.now() and szoba not in [f.szoba for f in self.szalloda.foglalasok if f.datum == datum]:
            self.szalloda.foglalasok.append(Foglalas(szoba, datum))
            return szoba.ar()
        else:
            return "A szoba nem érhető el ezen a dátumon."

    def lemondas(self, szoba, datum):
        for f in self.szalloda.foglalasok:
            if f.szoba == szoba and f.datum == datum:
                self.szalloda.foglalasok.remove(f)
                return "A foglalás lemondva."
        return "Nincs ilyen foglalás."

    def listazas(self):
        return [(f.szoba.szobaszam, f.datum) for f in self.szalloda.foglalasok]


szobak = [EgyagyasSzoba(i) if i % 2 == 0 else KetagyasSzoba(i) for i in range(1, 4)]
szalloda = Szalloda("Budapest Hotel", szobak)
kezelo = SzallodaKezelo(szalloda)

for i in range(5):
    print(kezelo.foglalas(szobak[i % 3], datetime(2024, 5, 7 + i)))

while True:
    print("1: Foglalás, 2: Lemondás, 3: Listázás")
    valasztas = input("Válassz egy műveletet: ")
    if valasztas == "1":
        szobaszam = int(input("Szobaszám: "))
        datum = datetime.strptime(input("Dátum (yyyy-mm-dd): "), "%Y-%m-%d")
        print(kezelo.foglalas(szobak[szobaszam - 1], datum))
    elif valasztas == "2":
        szobaszam = int(input("Szobaszám: "))
        datum = datetime.strptime(input("Dátum (yyyy-mm-dd): "), "%Y-%m-%d")
        print(kezelo.lemondas(szobak[szobaszam - 1], datum))
    elif valasztas == "3":
        print(kezelo.listazas())
