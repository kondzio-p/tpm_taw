'''
Porównanie pętli i list comprehension
Stwórz listę liczby składającą się z 1000 liczb losowych z zakresu 1 do 100
'''
import random
rd=random

lista_losowych_liczb = []

for i in range(1000):
    losowa_liczba = random.randint(1,100)
    lista_losowych_liczb.append(losowa_liczba)

print(lista_losowych_liczb)


#list comprehension

lista_losowych=[random.randint(1,100) for i in range(1000)]
print(lista_losowych)

#Zbuduj listę100 liczb rzeczywistych z zakresu 0-1
#metoda uniform z biblioteki random
listarz=[rd.uniform(0,1) for i in range(100)]
print(listarz)