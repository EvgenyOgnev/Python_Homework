# ****Задача 1.2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# ###--------V_1 при помощи for--------
import random

number = random.randint(100, 999)
sum = 0

for i in str(number):
    sum = sum + int(i)

print()
print(f'v_1) Сумма цифр трехзначного числа {number} = {sum}')


# ###--------V_2 при помощи математики--------

sum = number // 100 + number // 10 % 10 + number % 10

print()
print(f'v_2) Сумма цифр трехзначного числа {number} = {sum}')
