# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12



### V1 Первый вариант решения
import re

### Создаем переменные
dict_letter_price_ru = {} # создаем словарь буква - цена, русские буквы
dict_letter_price_en = {} # создаем словарь буква - цена, английские буквы
text = '0'

# лень в ручную заносить данные в словарь
list_letters_en = ['AEIOULNSTR', 'DG', 'BCMP', 'FHVWY', 'K', 'JX', 'QZ']

list_letters_ru = ['АВЕИНОРСТ', 'ДКЛМПУ', 'БГЁЬЯ', 'ЙЫ', 'ЖЗХЦЧ', 'ШЭЮ', 'ФЩЪ']

for i in range(len(list_letters_en)):
    for j in list_letters_en[i]:
        if i < 5:
            dict_letter_price_en[j] = i + 1
        elif i == 5:
            dict_letter_price_en[j] = 8
        elif i == 6:
            dict_letter_price_en[j] = 10
print(dict_letter_price_en)           

for i in range(len(list_letters_ru)):
    for j in list_letters_ru[i]:
        if i < 5:
            dict_letter_price_ru[j] = i + 1
        elif i == 5:
            dict_letter_price_ru[j] = 8
        elif i == 6:
            dict_letter_price_ru[j] = 10
print(dict_letter_price_ru)         

# ### проверка ввода

while text.isdigit():
    text = input('Введите слово: ').upper()
    if text.isdigit():
        print('Введите слово, а не число!')


### Поиск стоимости введеного слова:

if bool(re.search(r'[А-Я]', text)): # функции re.search загуглил
    print('V1) Стоимость слова', text, '=', sum(dict_letter_price_ru[k] for k in text))
else:
    print(f'V1) Стоимость слова {text}: {sum(dict_letter_price_en[k] for k in text)}')

### V2 Второй вариант решения, без проверки на каком языке вводиться слово, с общим словарем

### Словарь
dict_letter_price_ru_en = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}

### Поиск стоимости введеного слова:

print('V2) Стоимость слова', text, '=', sum([k for i in text for k, v in dict_letter_price_ru_en.items() if i in v]))












