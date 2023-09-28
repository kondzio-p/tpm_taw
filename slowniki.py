'''
Dictionary
key : value
'''

slownik1 = {'imie':'Anna','wiek':18, 'wzrost':1.76}
print(type(slownik1))
print(f"Mój słownik to: {slownik1}")

print(f"Klucze: {slownik1.keys()}")
print(f"Wartości: {slownik1.values}")

#print(f"Wiek: {slownik1['wiek']}")
#print(f"Wiek: {slownik1.get('wiek')}")

print(f"Słownik: {slownik1.items}")