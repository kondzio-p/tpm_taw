from random import uniform as rdu
import math
import matplotlib.pyplot as plt

def sposob1(liczby):
    zakresy = [ -10, -5, 0, 5, 10 ]
    plt.hist(liczby, bins = zakresy, color="lightblue", ec="red")
    plt.title(f"Histogram z liczb rzeczywistych w zakresie {zakresy}")
    plt.xlabel("liczby")
    plt.ylabel("Ilość liczb w zakresie")
    plt.xticks(zakresy)
    plt.show()

def sposob2(liczby, zakresy):
    wystapiena = { i : 0 for i in range(len(zakresy)-1)}
    for liczba in liczby:
        for i in range(len(zakresy)-1):
            if zakresy[i] <= liczba < zakresy[i+1]:
                wystapiena[i]+=1
    szer = (zakresy[i+1] - zakresy[i])/2
    zakr = [zakresy[i] + szer for i in wystapiena.keys()]
    plt.bar(zakr, wystapiena.values(), width=szer*2, color="lightblue", ec="green")
    plt.title(f"Histogram z liczb rzeczywistych w zakresie {zakresy}")
    plt.xlabel("liczby")
    plt.ylabel("Ilość liczb w zakresie")
    plt.xticks(zakresy)
    plt.show()


def generator(n,d,g):
    if d > g: d,g = g,d
    return[rdu(d,g) for i in range(n)]
    pass

def main():
    zakresy = [ -10, -5, 0, 5, 10 ]
    liczby = generator(100,-10,10)
    print(f"Liczby to {liczby}")
    sposob1(liczby)
    sposob2(liczby, zakresy)

if __name__ == "__main__":
    main()