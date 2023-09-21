'''
Title: Typ sekwencyjny - listy
'''

'''
lista1 = [1,2,3,4,5]
lista2 = [1,2,3, "tekst"]
lista3 = [1,2,3.4,[1,2,"coś"]]

print(type(lista1))
print(type(lista2))
print(type(lista3))

print(type(lista2[1]))
print(lista3[3][-1])

#lewa 0 1 2 3 4 5...
#prawa ... -4 -3 -2 -1

print(lista2[-1])
'''

moja_lista=[1,4,2,5,3,6,3]
print(moja_lista[1:4])

print(moja_lista[-2:-5:-1])
print(moja_lista[::-2])

nowa = ['a','b','c','d','e','f']
print(nowa[1::2]) #B D F  [START:KONIEC:KROK]
print(nowa[-2::-2])
print(nowa[-1::-2])