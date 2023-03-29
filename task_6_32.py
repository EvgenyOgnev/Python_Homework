
# # *Задача* 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

list1 = []
listIndex = []
maxNum = ''
minNum = ''
flag = True

while flag:
    try:
        maxNum = int(input("Введите максимальное значение от -5 до 10: "))
        minNum = int(input("Введите минимальное значение от -5 до 10: "))
        if maxNum < minNum:
            print('>>> Максимальное значение должно быть больше минимальное значение!')
        elif maxNum < -5 or maxNum > 10 or minNum < -5 or minNum > 10:
            print('>>> Введите значение от -5 до 10!')
        else:
            flag = False
    except:
        print(">>> Некорректный ввод. Попробуйте еще раз!")


list1 = [random.randint(-5, 10) for _ in range(21)]
print(list1)
print(minNum, maxNum)

listIndex = [i for i in range(len(list1)) if minNum <= list1[i] <= maxNum]
print(listIndex)
