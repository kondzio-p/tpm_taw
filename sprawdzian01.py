# Sprawdzian 01 liczby, listy, krotki
# Konrad Pepliński
# 3TPM
# 28.09.2023

#1
lista1=[2,4,6,'Anna','Zenon']
#2
print('Lista1: ', lista1)
#3
lista1.remove(4)
#4
lista1.append(99)
#5
lista2=[100,200,300]
#6
lista1.extend(lista2)
#7
print(lista1+lista2)
#8
lista2.reverse()
#9
print('Lista2: ', lista2)
#10
lista1.sort(key=lambda x: (isinstance(x, int), x))
#11
print('Lista1:', lista1)
#12
moja_tupla=('A','B','C')
#13
moja_tupla=moja_tupla + ('D',)
#14
print('Moja_tupla: ', moja_tupla)

# Używając list comprehension utwórz listę listaX składającą się z liczb
# nieparzystych z zakresu, który pobierzesz od użytkownika

poczatek_zakr = int(input("Podaj początek zakresu: "))
koniec_zakr = int(input("Podaj koniec zakresu: "))

listaX = [x for x in range(poczatek_zakr, koniec_zakr + 1) if x % 2 != 0]

print(listaX)