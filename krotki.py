'''
Typ sekwencyjny krótki - immutable!!!
'''

# moja_tupla = (3,4,5)
# print(type(moja_tupla))
# print(moja_tupla)

# moja_tupla2=moja_tupla
# print(moja_tupla2)

# lista=list(moja_tupla)
# lista.append(8)
# moja_tupla=tuple(lista)
# print(moja_tupla)

moja_tupla=(3,4,5)
lista=list(moja_tupla)
lista.append(6)
moja_tupla=tuple(lista)
print(moja_tupla)