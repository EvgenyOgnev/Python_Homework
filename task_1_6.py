# Задача 1.6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# ###--------V_1 при помощи for--------

ticketNumber = ''
sum1 = 0
sum2 = 0

while (not ticketNumber.isdigit() or len(ticketNumber) != 6):
    ticketNumber = input('Введите номер билета: ')
    if not ticketNumber.isdigit():
        print('.' * 11 + 'Введите, пожайлуста, числа')
    elif len(ticketNumber) != 6:
        print('.' * 11 + 'Введите, пожайлуста, шестизначный номер!')


for i in range(len(ticketNumber)):
    if i < (len(ticketNumber) / 2):
        sum1 += int(ticketNumber[i])
    elif i >= (len(ticketNumber) / 2):
        sum2 += int(ticketNumber[i])

# print(sum1, sum2)

if sum1 == sum2:
    print(f'v1) Билет с номером {ticketNumber} – счастливый')
else:
    print(f'v1) Билет с номером {ticketNumber} – обычный')

# ###--------V_2 при помощи математики-------

ticketNumber = int(ticketNumber)
summ1 = ticketNumber // 100000 + \
    ticketNumber // 10000 % 10 + ticketNumber // 1000 % 10
summ2 = ticketNumber // 100 % 10 + ticketNumber // 10 % 10 + ticketNumber % 10
# print(summ1, summ2)

if summ1 == summ2:
    print(f'v2) Билет с номером {ticketNumber} – счастливый')
else:
    print(f'v2) Билет с номером {ticketNumber} – обычный')
