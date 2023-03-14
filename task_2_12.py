# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:*
# 4 4 -> 2 2
# 5 6 -> 2 3


###   Петя задумывает два натуральных числа X и Y (X,Y≤1000)
import random

x = random.randint(1, 1000)
y = random.randint(1, 1000)
print(x, y)

### Петя называет сумму этих чисел и их произведение.
s = x + y
p = x * y
print(f'Cумму чисел = {s}. Произведение чисел = {p}') 

### Помогаем Кате отгадать задуманные Петей числа.
for i in range(1, s):
    if i * (s - i) == p:
        print(f'Загаданные числа: {i} и {s - i}')
        break
    
 
#  ##-----Решение с помощью системы уравнений (математический)------##

y1 = (s-(s**2 - 4 * p)**0.5) / 2
x1 = s - y1

print('Петя задумал числа:', int(x1), int(y1))
