'''
zbiory
'''

zb={2,5,1,3,5,1}
#print(zb)

zb.add(4)
zb.add(5)
print(zb)

zb.remove(2)
#print(zb)

#zb.remove(2) bedzie blad jesli nie ma elementu w zbiorze
#zb.discrad(2) tu nie bedzie bledu nawet jesli elemnen nie znajduje sie w zbiorze

a={1,3,5}
b={2,3,6}



suma=a.union(b)
print(suma)

roznica=a.difference(a)
print(roznica)

roznica2=b.difference(b)
print(roznica2)

if 3 in b:
    b.remove(3)

if 3 in b:
    b.remove(3)

    lista1=[2,4,5,6,9]
    if 1 in lista1:
        print("Jest")
    else:
        print("Nie ma")

listaX={2, 3, 4, 2, 3, 4, 2, 3, 4}
listaX=list(set(listaX))
print(listaX)
