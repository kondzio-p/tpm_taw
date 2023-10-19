'''
Metody sortowania
Konrad Pepliński
3TPM 
'''
from random import randint as rdint

# funkcja wyświetlająca menu
def menu():
    print(
        """
        Menu:
        b - bubble sort,
        i - inser sort,
        s - selection sort,
        q - quick sort
        """)

#dekorator pomiaru czasu
def pomiarczasu():
    pass

# bubble sort
def bubblesort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers            

#insert sort
def insertsort(numbers):
    for i in range(1,len(numbers)):
        j = i
        while numbers[j] < numbers[j-1] and j > 0:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            j -= 1
    return numbers
#selection sort (Barłomiej Labenz) 
def selectionsort():
    pass
#quicksort (Damian Kwasigroch)
def quicksort():
    pass
#pobieranie danych do generatora
def pobierz():
    pass
#generator liczb
def generator():
    print("====== Generowanie liczb =========")
    n = int(input("Podaj ilość liczb do generowania: "))
    while n == 0:
        print("Podałeś zero. ")
        n = int(input("Podaj ilość liczb do generowania: "))   
    
    d = int(input("Podaj dolny zakres liczb: "))
    g = int(input("Podaj górny zakres liczb: "))
    if d > g: d, g = g, d
    nums = [ rdint(d,g) for i in range(n) ]
    return nums 

def show(numbers, jakie= True):
    if jakie == True:
        print(f"\nLiczby przed sortowaniem to:") 
        print(numbers)   
    else:
        print(f"\nPosortowane liczby to:") 
        print(numbers)  
#główna funkcja aplikacji

def witaj():
    print("\n")
    print("=" * 50)
    print("Sortowanie liczb")
    print("=" * 50)
    
def main():
    czygen = True
    witaj()
    while True:
        if czygen == True:
            numbers_g = generator()
        menu()
        wybor = input("Wybierz metodą sortowania: ")
        if wybor in ('b', 'i', 's','q'):
            posort = []
            if wybor =='b':   
                liczby = numbers_g.copy()             
                show(liczby)
                posort = bubblesort(liczby)
                show(posort, False)
            elif wybor == 'i':
                liczby = numbers_g.copy()
                show(liczby)
                posort = insertsort(liczby)
                show(posort, False)
            elif wybor == 's':
                liczby = numbers_g.copy()
                show(liczby)
                posort = selectionsort(liczby)
                show(posort, False)
            elif wybor == 'q':
                liczby = numbers_g.copy()
                show(liczby)
                posort = quicksort(liczby)
                show(posort, False)
            else:
                print("Zły wybór...")
        
        koniec = input("Czy chesz kontynuować? (t/n)")
        if koniec in ('t', 'T', 'n', 'N'):
            if koniec != 't' and koniec != 'T':
                print(".... Dziękujemy za współpracę ...")
                break
            else:
                wyb = input("Czy chcesz wygenerować nowe liczby? (t/n)")
                if wyb in ('t', 'T', 'n', 'N'):
                    if wyb == 't' or wyb =='T':
                        czygen = True
                    else:
                        czygen = False
                else:
                    print("Wybierz t lub n...")
        else:
            print("Zły wybór....")
# =====================================
if __name__ == "__main__":
    main()   
        
            