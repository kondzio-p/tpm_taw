import random

# 1) Generowanie listy 1000 losowych liczb całkowitych i zapis do pliku
random_numbers = [random.randint(0, 1000) for _ in range(1000)]

with open("liczby.txt", "w") as file:
    for number in random_numbers:
        file.write(str(number) + "\n")

# Funkcje do analizy listy z pliku
def read_list_from_file(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]

def sum_of_elements(numbers):
    return sum(numbers)

def min_element(numbers):
    return min(numbers)

def max_element(numbers):
    return max(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        return (middle1 + middle2) / 2
    else:
        return sorted_numbers[n // 2]

def first_20_sorted(numbers):
    return sorted(numbers)[:20]

def product_of_elements(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def count_3_digit_numbers(numbers):
    return sum(1 for number in numbers if 100 <= number <= 999)

def most_common_number(numbers):
    from collections import Counter
    counts = Counter(numbers)
    most_common = counts.most_common(1)
    return most_common[0]

def unique_numbers(numbers):
    return [number for number in numbers if numbers.count(number) == 1]

def numbers_appearing_thrice(numbers):
    return [number for number in numbers if numbers.count(number) == 3]

def contains_21(numbers):
    return [number for number in numbers if '21' in str(number)]

def greater_than_800(numbers):
    return sum(1 for number in numbers if number > 800)

def three_smallest_and_largest(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[:3], sorted_numbers[-3:]

def remove_duplicates(numbers):
    return list(set(numbers))

def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers

def convert_to_strings(numbers):
    return [str(number) for number in numbers]

def count_occurrences(numbers):
    counts = {number: numbers.count(number) for number in numbers}
    return counts

def palindrome_numbers(numbers):
    return [number for number in numbers if str(number) == str(number)[::-1]]

def elements_in_range(numbers, a, b):
    return sum(1 for number in numbers if a <= number <= b)

def even_numbers(numbers):
    return sum(1 for number in numbers if number % 2 == 0)

def odd_numbers(numbers):
    return sum(1 for number in numbers if number % 2 != 0)

def segregate_numbers(numbers):
    even_numbers = sorted([number for number in numbers if number % 2 == 0])
    odd_numbers = sorted([number for number in numbers if number % 2 != 0], reverse=True)
    return even_numbers + odd_numbers

# 2) Tworzenie n-elementowej listy ciągów znakowych
n = int(input("Podaj liczbę elementów w liście: "))
x = int(input("Podaj długość ciągów znakowych: "))
string_list = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(x)) for _ in range(n)]

# Funkcje do analizy listy ciągów znakowych
def count_characters(string_list):
    return sum(len(s) for s in string_list)

def count_letter_k(string_list):
    return sum(s.count('k') for s in string_list)

def count_substring_kt(string_list):
    return sum(s.count('kt') for s in string_list)

def count_longer_than_s(string_list, s):
    return sum(1 for string in string_list if len(string) > s)

def add_a_and_z(string_list):
    return [f'a{s}z' for s in string_list]

# 3) Analiza tekstu Lorem Ipsum
# Wczytaj tekst z pliku
with open("lorem_ipsum.txt", "r") as file:
    lorem_ipsum_text = file.read()

# Funkcje do analizy tekstu
def count_characters_in_text(text, include_spaces=False):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))

def count_words(text):
    words = text.split()
    return len(words)

def count_punctuation(text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return sum(text.count(char) for char in punctuation)

def count_sentences(text):
    sentences = text.split('.')
    return len(sentences)

def sentences_to_list(text):
    sentences = text.split('.')
    return [s.strip() for s in sentences if s.strip()]

def most_common_word(text):
    words = text.split()
    from collections import Counter
    counts = Counter(words)
    most_common = counts.most_common(1)
    return most_common[0]

# 4) Wywołanie funkcji i wypisanie wyników
print("1) Analiza listy liczb:")
numbers = read_list_from_file("liczby.txt")
print("Suma wszystkich elementów:", sum_of_elements(numbers))
print("Najmniejszy element (wersja 1):", min_element(numbers))
print("Najmniejszy element (wersja 2):", min(numbers))
print("Największy element (wersja 1):", max_element(numbers))
print("Największy element (wersja 2):", max(numbers))
print("Mediana:", median(numbers))
print("Pierwsze 20 posortowanych:", first_20_sorted(numbers))
print("Iloczyn wszystkich elementów:", product_of_elements(numbers))
print("Ilość liczb 3-cyfrowych:", count_3_digit_numbers(numbers))
most_common = most_common_number(numbers)
print("Najczęściej występująca liczba:", most_common[0], "ilość:", most_common[1])
print("Liczby, które się nie powtarzają:", unique_numbers(numbers))
print("Liczby, które występują dokładnie 3 razy:", numbers_appearing_thrice(numbers))
print("Liczby zawierające 21:", contains_21(numbers))
print("Liczby większe niż 800:", greater_than_800(numbers))
three_smallest, three_largest = three_smallest_and_largest(numbers)
print("Trzy najmniejsze liczby:", three_smallest)
print("Trzy największe liczby:", three_largest)
unique_numbers_no_duplicates = remove_duplicates(numbers)
print("Ilość elementów po usunięciu duplikatów:", len(unique_numbers_no_duplicates))
shuffled_numbers = shuffle_list(numbers)
print("Lista po pomieszaniu elementów:", shuffled_numbers)
string_numbers = convert_to_strings(numbers)
print("Lista po konwersji na stringi:", string_numbers)
counted_numbers = count_occurrences(numbers)
print("Liczba wystąpień każdej liczby:", counted_numbers)
print("Liczby-palindromy:", palindrome_numbers(numbers))
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print("Ilość elementów w przedziale <", a, ",", b, ">: ", elements_in_range(numbers, a, b))
print("Ilość liczb parzystych:", even_numbers(numbers))
print("Ilość liczb nieparzystych:", odd_numbers(numbers))
segregated = segregate_numbers(numbers)
print("Lista po segregacji:", segregated)

print("\n2) Analiza listy ciągów znakowych:")
print("Ilość znaków w liście:", count_characters(string_list))
print("Ilość liter 'k' w liście:", count_letter_k(string_list))
print("Ilość ciągów 'kt' w liście:", count_substring_kt(string_list))
s = int(input("Podaj minimalną długość ciągów do zliczenia: "))
print("Ilość ciągów dłuższych niż", s, "znaków:", count_longer_than_s(string_list, s))
print("Lista po dodaniu 'a' na początku i 'z' na końcu:", add_a_and_z(string_list))

print("\n3) Analiza tekstu Lorem Ipsum:")
print("Ilość znaków w tekście (z spacjami):", count_characters_in_text(lorem_ipsum_text, include_spaces=True))
print("Ilość znaków w tekście (bez spacji):", count_characters_in_text(lorem_ipsum_text, include_spaces=False))
print("Ilość słów w tekście:", count_words(lorem_ipsum_text))
print("Ilość znaków interpunkcyjnych w tekście:", count_punctuation(lorem_ipsum_text))
print("Ilość zdań w tekście:", count_sentences(lorem_ipsum_text))
print("Zdania w tekście:")
for sentence in sentences_to_list(lorem_ipsum_text):
    print(sentence)
most_common = most_common_word(lorem_ipsum_text)
print("Najczęściej występujący wyraz:", most_common[0], "ilość:", most_common[1])
