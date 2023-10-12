'''
Cwiczenia z funkcji
'''

#Obliczanie średniej arytmetycznej
#Napisz funkcję, która przyjmie listę liczb i zwróci ich średnią arytmetyczną

# def srednia(lista):
#     ilosc = len(lista)
#     suma=sum(lista)
#     if ilosc==0:
#         return 0
#     else:
#         return suma/ilosc
    
# liczby=[2,3,5,3,5]
# print(srednia(liczby))

# def srednia2(*args):
#     suma = 0
#     ilosc = len(args)
#     if ilosc==0:
#         return "Nie można dzielić przez 0"
#     else:
#         for i in args:
#             suma += i
#     return suma/ilosc

# print(srednia2(3,4,2,2,5))

# def staty(tekst):
#     ilosc={'litery':0, 'liczby':0,'spacje':0,'wyrazy':0}
#     for litera in tekst:
#         if litera.isalpha():
#             ilosc['litery'] +=1
#         elif litera.isdigit():
#             ilosc['liczby'] +=1
#         elif litera.isspace():
#             ilosc['spacje'] +=1
    
#     wyrazy = tekst.split()
#     ilosc['wyrazy'] = len(wyrazy)
#     return ilosc

# tekst=input("podaj tekst")
# print(f"Liczba liter w tekście to {staty(tekst)}")

'''
liczby = [1,2,3,4,5]
kwadraty = list(map(lambda x: x ** 2, liczby))
print(kwadraty)
'''

# liczby = [1,2,3,4,5]
# parzyste = list(filter(lambda x: x%2==0, liczby))
# print(parzyste)

# slowa = ["jabłko", "banan", "truskawka", "gruszka", "malina"]
# slowa_posortowane = sorted(slowa, key=lambda x: len(x))
# print(slowa_posortowane)

# dane = [(1,5),(3,2),(2,8),(4,1)]
# dane_posortowane = sorted(dane, key=lambda x: x[1])
# print(dane_posortowane)

# slowa = ["jabłko", "banan", "truskawka", "gruszka", "malina"]
# litera = 'b'
# slowa_filtr = list(filter(lambda x: x.startwith(litera), slowa))
# print(slowa_filtr)

# slowa = ["jabłko", "banan", "truskawka", "gruszka", "malina"]

# litera_p="b"
# litera_k="a"

# print(list(filter(lambda x: x.startswith(litera_p), slowa)))
# print(list(filter(lambda x: x.endswith(litera_k), slowa)))

boki = [3,4,5]
wysokosci=[4,5,6]
#lambda + map

pole=list(map(lambda x, y: 0.5*x*y, boki, wysokosci))
print(pole)