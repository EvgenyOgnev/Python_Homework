# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:*
# 5 -> 1 0 1 1 0
# 2

import random
st = True
n = None
nList = [] # Перечень монет, некоторые из них лежат вверх решкой, а некоторые – гербом.
n0 = 0 # Количество монет лежащих вверх гербом
n1 = 0 # Количество монет лежащих вверх решкой

# ## Поверка павильности ввода количества монет
while st:
    try:
        n = int(input('Введите количество монет: '))
        if n <= 0:
            print('Монет не может быть меньше или равно нулю, попробуйте еще раз!')
        elif n == 1:
            print(
                'Монета одна и переворачивать нечего!\n   Введите количество больше одной!')
        else:
            st = False
    except:
        print('Некорректный ввод. Попробуйте еще раз!')


# ## Рандомный разброс монет: 1 - вверх решкой, 0 - вверх гербом.
for _ in range(n):
    nList.append(random.randint(0, 1))
print(*nList)


## Ведем подсчет и ищем минимальное количество монет лежащих вверх решкой или гербом

for i in nList:
    if i == 0:
        n0 += 1
    else:
        n1 +=1

# print(f'0 = {n0}...... 1 = {n1}')

if n0 == 0 or n1 == 0:
    print('Переворачивать нечего!!!')
elif n0 == n1:
    print(f'Переверните любые монеты лежащих вверх гербом или решкой: {n0} шт.')
elif n0 < n1:
    print(f'Переверните монеты с гербом в количестве: {n0} шт.')
else:
    print(f'Переверните монеты с решкой в количестве: {n1} шт.')