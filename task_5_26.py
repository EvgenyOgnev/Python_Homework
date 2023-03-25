
# 	*Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = ''
b = ''
flag = True

def aRaisePowerB(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * (aRaisePowerB(a, b - 1))


while flag:
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите степень числа: '))
        if b < 0:
            print('!' * 5 + ' >>> ' + 'Введите степень больше ноля!') 
        else:
            flag = False
    except:
        print('!!! >>> Некорректный ввод! Попробуйте еще раз!')
        

print(aRaisePowerB(a, b))

