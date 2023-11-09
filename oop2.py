class Klient():
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stan_konta = 250000

    def wypisz_klient(self):
        return f"Klient to {self.imie} {self.nazwisko}"

    def zwieksz_stan(self, kwota):
        if kwota<=0:
            print("Nie masz nic na koncie")
        else:
            self.stan_konta+=kwota
        return self.stan_konta
    
    def pokaz_stan(self):
       return f"Stan konta wynosi {self.stan_konta}"
    
def main():
    klient1 = Klient("Jan", "Kowalski")
    print(klient1.wypisz_klient())
    print(klient1.pokaz_stan())
    klient1.zwieksz_stan(200)
    print(klient1.pokaz_stan())

if __name__ == '__main__':
    main()