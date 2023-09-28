'''
Dictonary
key : value
'''

slownik={'imie': 'Anna', 'wiek':18,'wzrost':1.76}
#print(type(slownik))
#print(f"Moj slownik to: {slownik}")

#print(f"Klucze: {slownik.keys()}")
#print(f"Wartosci to: {slownik.values()}") 

#print(f"Wiek: {slownik['wiek']}")
#print(f"Wiek: {slownik.get('wiek')}")

#print(f"Slownik: {slownik.items()}")

#for k, v in slownik.items():
#    print(f"{k} -{v}")

#slownik.pop('wiek')
#print(slownik)
#slownik['wiek']=18
#print(slownik)


#slownik['wiek'], slownik['wzrostt']=slownik['wzrost'],slownik['wiek']
#print(slownik.items())

#tup=('miejscowosc','Chojnice')
#print(tup)
#slownik[tup[0]]=tup[1]
#print(slownik)


li=list(slownik.items())
li[1],li[2],=li[2],li[1]
slownik=dict(li)
print(slownik.items())


