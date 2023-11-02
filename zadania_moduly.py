from m_zapis_odczyt import zapis

tekst = """
    Pierwsza linia
    Druga linia
    Trzecia linia
"""

#liczby = [i**2 for i in range(100)]
liczby = [3, 4, "rower", 4, "Ania"]
sl={"imie" : "Jan", "nazwisko" : "Kowalski"}

zapis("tekst.txt", "wt", "txt", tekst)
zapis("liczby.txt", "wt", "lista", liczby)
zapis("slownik.txt", "wt", "slownik", sl)