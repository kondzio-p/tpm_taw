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