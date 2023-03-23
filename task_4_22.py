#     Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Ввод:   11 6
#         2 4 6 8 10 12 10 8 6 4 2
#         3 6 9 12 15 18
# Вывод:  6 12

# Создаем переменные
n = 0
m = 0
flag = True
list_numbers_n = []
list_numbers_m = []
list_num_n_m = []

# ## Поверка павильности ввода количества элементов множеств

while flag:
    try:
        n = int(input('Введите количество элементов первого множества: '))
        list_numbers_n = input(
            f'Введите элементы {n} шт. через пробел: ').split(' ')
        list_numbers_n = [int(i) for i in list_numbers_n if i != '']
        if n <= 0:
            print('Элементов не может быть равно нолю или меньше ноля!')
        elif len(list_numbers_n) < n or len(list_numbers_n) > n:
            print(f'Ввели не верное количество элементов!')
        else:
            flag = False
    except:
        print('Некорректный ввод. Попробуйте еще раз!')

flag = True

while flag:
    try:
        m = int(input('Введите количество элементов второго множества: '))
        list_numbers_m = input(
            f'Введите элементы {m} шт. через пробел: ').split(' ')
        list_numbers_m = [int(i) for i in list_numbers_m if i != '']
        if m <= 0:
            print('Элементов не может быть равно нолю или меньше ноля!')
        elif len(list_numbers_m) < m or len(list_numbers_m) > m:
            print(f'    Ввели не верное количество элементов!')
        else:
            flag = False
    except:
        print('Некорректный ввод. Попробуйте еще раз!')

print(list_numbers_n)
print(list_numbers_m)

# С помощью операций со множествами находим пересечение множеств, функция .intersection()
list_num_n_m = list(set(list_numbers_n).intersection(set(list_numbers_m)))
print(list_num_n_m)

# Проверяем кол-во элементов пересечения множеств, и выставляем в порядке возрастания
if len(list_num_n_m) == 0:
    print('\n   Пересечений множеств отсутствует!')
elif len(list_num_n_m) == 1:
    print('\n   Число, которое встречается в обоих множествах:', *list_num_n_m)
elif len(list_num_n_m) > 1:
    for i in range(len(list_num_n_m) - 1):
        j = list_num_n_m.index(min(list_num_n_m[i:]))
        list_num_n_m[i], list_num_n_m[j] = min(
            list_num_n_m[i:]), list_num_n_m[i]
    print('\n   Числа, которые встречаются в обоих множествах:', *list_num_n_m)
