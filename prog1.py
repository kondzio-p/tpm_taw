from moj_modul import dodawanie
from moj_modul import potegowanie

a = int(input("Podaj liczbę: "))
b = int(input("Podaj drugą liczbę: "))

potega = potegowanie(a, b)
print(f"Potęga {a} do {b} to {potega}")
print(f"Suma {a} i {b} to {dodawanie}")