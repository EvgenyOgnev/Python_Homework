# ## Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X. Заполните массив случайными натуральными числами от 1 до N/2. Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random

n = None  # Количество элементов в массиве
x = None  # Число, которое проверяем
list_n = []  # Перечень элементов
flag = True

# ## Проверка ввода
while flag:
    try:
        n = int(input('Введите количество элементов: '))
        x = int(input('Введите число для проверки: '))
        if n <= 1:
            print('При количестве элементов < 1, нечего считать!')
        elif x < 1:
            print('Вводите числа для проверки больше 0!')
        else:
            flag = False
    except:
        print('Не коректный ввод. Пробуйте еще раз!')

# ## Наполнение списка элементами

list_n = [random.randint(1, n//2) for i in range(n)]
print(list_n)

# ## V_1 - первый вариант решения

j = 0
count_1 = 0
while j < n:
    if x == list_n[j]:
        count_1 += 1
    j +=1
  

if count_1 % 10 == 2 or count_1 % 10 == 3 or count_1 % 10 == 4:
    if count_1 // 10 % 10 == 1:
        print(f'V_1) {x} встречаеться в массиве - {count_1} раз')
    else:
        print(f'V_1) {x} встречаеться в массиве - {count_1} разa')   
else:
    print(f'V_1) {x} встречаеться в массиве - {count_1} раз')
    
    
# ##V_2 - второй вариант решения

count_2 = 0
for i in list_n:
    if x == i:
        count_2 += 1


if str(count_2)[-1] == '2' or str(count_2)[-1] == '3' or str(count_2)[-1] == '4':
    if len(str(count_2)) == 1:
        print(f'V_2) {count_2} разa - в массиве встречаеться {x}')
    elif str(count_2)[-2] == '1':
        print(f'V_2) {count_2} раз - в массиве встречаеться {x}')
    else:
        print(f'V_2) {count_2} разa - в массиве встречаеться {x}')
else:
    print(f'V_2) {count_2} раз - в массиве встречаеться {x}')
        


# ## V_3 - третий вариант решения

count_3 = list_n.count(x)

if str(count_3)[-1] == '2' or str(count_3)[-1] == '3' or str(count_3)[-1] == '4':
    if count_3 // 10 % 10 == 1:
        print(f'V_3) {x} встречаеться в массиве - {count_3} раз')
    else:
        print(f'V_3) {x} встречаеться в массиве - {count_3} разa')   
else:
    print(f'V_3) {x} встречаеться в массиве - {count_3} раз')

