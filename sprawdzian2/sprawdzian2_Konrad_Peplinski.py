'''
Konrad Pepliński
3TPM
26.10.2023
'''
import random

def minimum(arr: list):
    if not arr:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

def iloczyn(arr: list):
    iloczyn = 1
    for i in arr:
        iloczyn *= i
    return iloczyn

def oblicz_statystyki(liczby):
    statystyki = {}
    statystyki["suma"] = sum(liczby)
    statystyki["iloczyn"] = iloczyn(liczby)
    statystyki["średnia"] = sum(liczby) / len(liczby)
    statystyki["maksymalna liczba"] = max(liczby)
    statystyki["minimalna liczba"] = minimum(liczby)
    statystyki["najczęściej występująca liczba"] = max(set(liczby), key=liczby.count)
    return statystyki

def znajdz_kody_ascii(liczby):
    kody = []
    for idx, num in enumerate(liczby, start=1):
        if 32 <= num <= 126:
            char = chr(num)
            kody.append((char, idx))
    return kody

try:
    # Generowanie 1000 losowych liczb i zapis do pliku
    with open("liczby.txt", "w") as file:
        for _ in range(1000):
            num = random.randint(1, 100)
            file.write(f"{num}\n")
except IOError as err:
    print(f"Błąd podczas zapisu do pliku: {err}")

try:
    # Wczytywanie liczb z pliku
    with open("liczby.txt", "r") as file:
        liczby = [int(line.strip()) for line in file]
except IOError as err:
    print(f"Błąd podczas odczytu pliku: {err}")

# Obliczanie statystyk
statystyki = oblicz_statystyki(liczby)

# Zapis statystyk do pliku
try:
    with open("staty.txt", "w") as stat_file:
        for key, value in statystyki.items():
            stat_file.write(f"{key} - {value}\n")
except IOError as err:
    print(f"Błąd podczas zapisu statystyk: {err}")

# Znajdowanie kodów ASCII
kody_ascii = znajdz_kody_ascii(liczby)

# Zapis kodów ASCII do pliku
try:
    with open("kody.txt", "w") as kod_file:
        for char, idx in kody_ascii:
            kod_file.write(f"{char} w linijce {idx}\n")
except IOError as err:
    print(f"Błąd podczas zapisu kodów ASCII: {err}")
