'''
Zad. 1 Napisz aplikację konsolową pobierającą od użytkownika jego datę narodzin, a następnie wyznaczającą datę
najbliższych urodzin, liczbę dni do najbliższych urodzin.
'''
from datetime import datetime

def pobierz_date_urodzenia():
    while True:
        try:
            data_urodzenia = input("Podaj datę narodzin (RRRR-MM-DD)")
            data_urodzenia=datetime.strptime(data_urodzenia, "%Y-%m-%d")
            return data_urodzenia
        except ValueError as e:
            print('Niepoprawne formatowanie daty')

def wyznacz_najblizsze_urodziny(data_urodzenia):
    obecna_data=datetime.now()
    aktualne_urodziny=datetime(obecna_data.year, data_urodzenia.month, data_urodzenia.day)
    if obecna_data > aktualne_urodziny:
        najblizsze_urodziny = datetime(obecna_data.year + 1, data_urodzenia.month, data_urodzenia.day)
    else:
        najblizsze_urodziny = aktualne_urodziny
    liczba_dni=(najblizsze_urodziny - obecna_data).days
    
    return najblizsze_urodziny, liczba_dni
def main():
    print("Program do obliczania liczby dni do urodzin")
    data_urodzenia=pobierz_date_urodzenia()
    print(f"Twoje narodziny były {data_urodzenia}")
    najblizsze_urodziny, liczba_dni=wyznacz_najblizsze_urodziny(data_urodzenia)
    print(f"Najbliższe urodziny: ", najblizsze_urodziny.strftime("%Y-%m-%d"))
    print(f"Liczba dni do najlbiższych urodzin: {liczba_dni}")

if __name__ == "__main__":
    main()