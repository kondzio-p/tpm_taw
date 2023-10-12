'''
Funkcje python
'''

def menu():
    print(f"Wybór: d-dodawania, o-odejmowanie, dz-dzielenie, m-mnożenie")

def kalkulator(dzialanie,a,b):
    if dzialanie=="d":
        return a+b
    elif dzialanie=="o":
        return a-b
    elif dzialanie=="m":
        return a*b
    elif dzialanie=="s":
        if b!=0:
            return a/b
        else: return "Nie dzielę przez 0"
    else:
        return "Zły wybór działania"
    return True
def f_main():
    a= float(input("Podaj pierwszą liczbę"))
    b= float(input("Podaj drugą liczbę"))
    menu()
    dzialanie=input()

    print(f"Wynikiem dzialania {dzialanie} dla liczb {a} i {b} jest {kalkulator(dzialanie,a,b)}")

#================
f_main()