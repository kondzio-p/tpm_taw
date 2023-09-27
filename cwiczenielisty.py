#------------------------------#
#Autor: Konrad Pepliński
#Opis programu: Listy
#------------------------------#
moja_lista = []
moja_lista.extend([3,3,8,9,2,5,7])
print(moja_lista)
moja_lista.remove(8)
print(moja_lista)
print(moja_lista[-2::-2])
moja_lista.insert(3,7)
print(moja_lista)
n=len(moja_lista)
print(f"dlugosc listy to:{n}")
zlicz=moja_lista.count(7)
print(zlicz)



lista2=[1, 3, 5, 7]
print(lista2)
moja_lista.extend(lista2)
print(moja_lista)
n=len(moja_lista)
print(f"dlugosc listy to:{n}")

moja_tupla=(33,55,77)

lista=list(moja_tupla)
nowa_tupla=moja_tupla+tuple(moja_lista)
posortowana_tupla=tuple(sorted(nowa_tupla))
print(posortowana_tupla)


lista2.reverse()
print(lista2)