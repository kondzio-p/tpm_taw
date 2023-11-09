class Samochod():
    def __init__(self, marka, model, rocznik, pojemnosc_silnika, przebieg, wlasciciel):
        self.marka=marka
        self.model=model
        self.rocznik=rocznik
        self.pojemnosc_silnika=pojemnosc_silnika
        self.przebieg=przebieg
        self.wlasciciel=wlasciciel
    
    def pokaz_samochod(self):
        return f"Atrybuty samochodu: {self.marka} | {self.model} | {self.rocznik} | {self.pojemnosc_silnika} | {self.przebieg} | {self.wlasciciel}"

    def zmien_przebieg(self, km):
        self.przebieg+=km
        return self.przebieg
    
    def zmien_wlasciciela(self, x):
        self.wlasciciel = x
        return self.wlasciciel
        
    def zapisz_samochod(self):
        with open("pojazdy.txt", "a") as file:
            file.write(f"{self.marka} | {self.model} | {self.rocznik} | {self.pojemnosc_silnika} | {self.przebieg} | {self.wlasciciel}\n")




def main():
    pojazd1 = Samochod("BMW", "428XI", 2020, 2, 8772, "Jan Kowalski")
    pojazd1.zmien_wlasciciela("Tomasz Nowak")
    print(pojazd1.pokaz_samochod())
    pojazd1.zapisz_samochod()

if __name__ == '__main__':
    main()
