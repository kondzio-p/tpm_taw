class Osoba:
    def __init__(self, imie, nazwisko, wiek=16):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def przedstaw_sie(self):
        return f"Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat."
    
    def zwieksz_wiek(self,ile=0):
        self.wiek += ile
        return self.wiek
    
class Uczen(Osoba):
    def __init__(self, imie, nazwisko, wiek, klasa):
        super().__init__(imie, nazwisko, wiek)
        self.klasa = klasa
    
    def przedstaw_sie(self):
        return f"Jestem uczniem i nazywam się {self.imie} {self.nazwisko} i chodze do klasy {self.klasa}"
    
class Nauczyciel(Osoba):
    def __init__(self, imie, nazwisko, wiek, przedmiot):
        super().__init__(imie, nazwisko, wiek)
        self.przedmiot = przedmiot
        self.wyplata=1

    def przedstaw_sie(self):
        return f"Nazywam sie {self.imie} {self.nazwisko}, jestem nauczycielem a i uczę {self.przedmiot}"

    def zwieksz(self, kwota):
        self.wyplata+=kwota
        return self.wyplata
    
    def pokaz_wyplate(self):
        return f'Obecna wyplata to: {self.wyplata}'
def przywitanie(osoby):
    return osoby.przedstaw_sie()
#-------------
def main():
    osoba1 = Osoba("Adam", "Nowak", 17)
    osoba1.przedstaw_sie()
    osoba1.zwieksz_wiek(3)
    print(osoba1.przedstaw_sie())

    uczen1=Uczen("Jan", "Kowalski", 16, "3TPM")
    print(uczen1.przedstaw_sie())

    nauczyciel1=Nauczyciel("Barbara", "Tomasiewicz", 34, "Jezyk Polski")
    print(nauczyciel1.przedstaw_sie())

    print(przywitanie(osoba1))
    print(przywitanie(nauczyciel1))

    print(nauczyciel1.pokaz_wyplate())
    nauczyciel1.zwieksz(500)
    print(nauczyciel1.pokaz_wyplate())

if __name__ == '__main__':
    main()