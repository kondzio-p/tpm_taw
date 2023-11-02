# Funkcja do zapisu danych do pliku
def zapis(nazwapliku, tryb, rodzaj, tresc):
    try:
        with open(nazwapliku, tryb) as plik:
            if rodzaj in ("txt","lista","slownik"):
                if rodzaj=='txt':
                    plik.write(tresc)
                elif rodzaj == 'lista':
                    [
                        plik.write(i+"\n") if isinstance(i, str) \
                            else plik.write(str(i)+"\n") for i in tresc
                    ]
                    
                else:
                    [
                        plik.write(k+" : " + str(v) + "\n" for k,v in tresc.items())
                    ]
                                        
                print(f"Zawartość została zapisana do {nazwapliku}")
            else:
                print(f"Nie potrafię obsłużyć pliku z danymi: {rodzaj}")
          
    except Exception as e:
        print(f"Błąd zapisu do pliku: {e}")

# Funkcja do odczytu danych z pliku
def odczyt(nazwapliku, tryb, rodzaj):
    try:
        with open(nazwapliku, tryb) as plik:
            if rodzaj == "tekst":
                return plik.read()
            elif rodzaj == "liczby":
                return float(plik.read())
            elif rodzaj == "slowniki":
                wynik = {}
                for linia in plik:
                    k, v = linia.strip().split(":")
                    wynik[k] = v
                return wynik
            else:
                print("Nieobsługiwany rodzaj danych")
                return None
    except Exception as e:
        print(f"Błąd odczytu pliku: {e}")
